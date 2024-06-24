# Netbox
## HPCCF's Source of Truth
[HPCCF's Netbox Site](https://netbox.hpc.ucdavis.edu/dcim/sites/)

NetBox is an infrastructure resource modeling (IRM) application designed to empower network automation. NetBox was developed specifically to address the needs of network and infrastructure engineers.

## Netbox Features

- Comprehensive Data Model
- Focused Development
- Extensible and Customizable
- Flexible Permissions
- Custom Validation & Protection Rules
- Device Configuration Rendering
- Custom Scripts
- Automated Events
- Comprehensive Change Logging

## Netbox Administration

- This section will give an overview of how HPCCF admins utilize and administer Netbox

### How to add assets into Netbox

1. Navigate to HPCCF's Netbox instance here: [HPCCF's Netbox Site](https://netbox.hpc.ucdavis.edu/dcim/sites/) ![1](../img/netbox1.jpeg)
2. Select the site to which you will be adding an asset too. In this example I have chosen Campus DC: ![2](../img/netbox2.jpeg)
3. Scroll down to the bottom of this page and select which of the locations you will add your asset too, here I chose the Storage Cabinet: ![3](../img/netbox3.jpeg) ![4](../img/netbox4.jpeg)
4. On this page scroll to the bottom and select Add a Device: ![5](../img/netbox5.jpeg)
5. After you have selected Add a Device you should see a page like this: ![6](../img/netbox6.jpeg)
6. Fill out this page with specifics of the asset, some fields are not required but try to fill out this section as much as possible with the fields available, here is an example of a created asset and how it should look: ![7](../img/netbox7.jpeg)![8](../img/netbox8.jpeg)![9](../img/netbox9.jpeg)![10](../img/netbox10.jpeg)![11](../img/netbox11.jpeg)![12](../img/netbox12.jpeg)![13](../img/netbox13.jpeg)
7. Ensure to click on Save to have the device added.

### How to add components to an Asset

1. On the asset page select the + Add Components dropdown and select the component you wish to add, for this I have chosen a Console Port: ![14](../img/netbox14.jpeg)
2. Here again you will fill out the dropdowns as thoroughly as possible, the example here is of an interface that has already been added: ![15](../img/netbox15.jpeg)![16](../img/netbox16.jpeg)![17](../img/netbox17.jpeg)![18](../img/netbox18.jpeg)
3. Again make sure to click Save to ensure the component has been added.
4. This process can be used to add all of the following componentes to a device:![netbox19](../img/netbox19.jpeg)