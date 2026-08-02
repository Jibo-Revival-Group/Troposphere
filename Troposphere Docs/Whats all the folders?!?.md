- - -
So Generally the project is structured in this way to accommodate for the build tool that bundles and compiles everything into a single install sequence... what im trying to say is its made for modularity first!


# Lets get started with `/` 

Any directory that is aware by the bundler is ==^Highlighted==

## The `art` Directory
Thats Where you put art... doesnt really get used in the bundler but might get used in the future!

## The `DevTools`
- - -

So DevTools consist of programs that intend to help with the development of Troposphere s.a: 

`Build_Project` -> Actual bundler & compiler
`JiboSync` -> WIP , sync files and dynamically update the environment
`sll` -> Simple Logging Library for python
`TreeLib` -> Library to create fancy trees :)

## `examples`

The examples directory will host a bunch of examples using the troposphere library , but still a WIP


## ==^include== directory

Thats parts of the bundler that will be included into the final port and each sub directory plays a different role on where it will correspond in the root of the robot

### `dual_rootfs` and `dualrootfs.tar.gz`
This is a regular Linux system tree (UN initialized)

### `root`
The root directory represents the robots root directory and any path inside will be resolved into the robot, ->>> ==Conflicting files will always be overwritten by tropospheres bundle ==<<<- 


### `root_cfg` - To be discontinued 

### `shell`
In shell are only troposphere related files and , while they will not always resolve directly to the root tree instead the bundler decides where these would be located




## `output`

Thats where the final builds & bundled binaries will end, copy that folder onto a robot and run the equivalent to `install.sh`

## ==^troposphere_lib==

Thats the standard library for troposphere

## ==^splash_0.png==

This will be the boot splash on the bundled output