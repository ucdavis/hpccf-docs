import os
import pathlib
import re
import yaml


def parse_spack_index(modulefiles_path):
    with open(os.path.join(modulefiles_path, 'module-index.yaml')) as fp:
        module_index = yaml.load(fp, yaml.SafeLoader)['module_index']
    return module_index


def build_module_data(module_index, modulefiles_path):
    modules = {}
    for pkg_hash in module_index:
        name = module_index[pkg_hash]['use_name'].split('/')
        path = pathlib.PurePath(module_index[pkg_hash]['path'])
        relpath = pathlib.PurePath(os.path.join(*path.parts[5:]))
        path = modulefiles_path / relpath

        fullname = os.path.join(*name)
        software = name[0]
        version, _, arch = name[-1].partition('+')
        build = None if len(name) == 2 else name[1]

        if software not in modules:
            modules[software] = {}
            modules[software]['variants'] = {}
            modules[software]['versions'] = set()
            modules[software]['builds'] = set()
            modules[software]['arches'] = set()

        entry = modules[software]
        entry['versions'].add(version)
        entry['variants'][fullname] = path
        if build:
            entry['builds'].add(build)
        if arch:
            entry['arches'].add(arch)
    
    return modules


def render_spack_modules(modules):
    entries = []
    for software, entry in sorted(modules.items()):
        path = list(entry['variants'].values())[-1]
        versions = ', '.join(entry['versions'])
        variants = ', '.join(entry['builds'])
        modulenames = ', '.join((f'`{name}`' for name in entry['variants'].keys()))

        arches = entry['arches']
        if not arches:
            arches.add('generic')
        arches = ', '.join(arches)

        with open(path) as fp:
            contents = fp.read()
            about = re.search(r'help\(\[\[([^\]]*)\]\]\)', contents, flags=re.MULTILINE).group(1)
        
        entries.append(( f'## {software}\n\n'
                         f'{about}\n\n'
                         f'**Versions**: {versions}\n\n'
                         f'{"**Variants**: " if variants else ""}{variants}\n\n'
                         f'**Arches**: {arches}\n\n'
                         f'**Modules**: {modulenames}'))
        
    return '\n'.join(entries)


def define_env(env):
    @env.macro
    def spack_modules_list():
        path = pathlib.PurePath(env.variables['spack_modulefiles_path'])
        modules = build_module_data(parse_spack_index(path), path)
        rendered = render_spack_modules(modules)
        return rendered
