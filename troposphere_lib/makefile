CC = arm-none-linux-gnueabihf-gcc

# Compiler flags (-Iinclude tells it where your headers are)
CFLAGS = -Wall -fPIC -O2 -mcpu=cortex-a15 -mfloat-abi=hard -mfpu=vfpv4 -Iinclude

# Directory configuration
SRC_DIR = src
BUILD_DIR = build

# Find all .c files in src/ and src/dev/
SRCS = $(wildcard $(SRC_DIR)/*.c) $(wildcard $(SRC_DIR)/dev/*.c)

# Convert source file paths to build file paths
# Example: src/dev/fan_pwm.c -> build/dev/fan_pwm.o
OBJS = $(patsubst $(SRC_DIR)/%.c, $(BUILD_DIR)/%.o, $(SRCS))

# The final library output location
TARGET = $(BUILD_DIR)/libtroposphere.so

.PHONY: all clean

all: $(TARGET)

# Link the shared library from the object files inside the build directory
$(TARGET): $(OBJS)
	@mkdir -p $(dir $@)
	$(CC) -shared -o $@ $(OBJS)
	@echo "Successfully built target: $@"

# Rule to compile .c files into .o files inside the build directory
$(BUILD_DIR)/%.o: $(SRC_DIR)/%.c
	@mkdir -p $(dir $@)
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	@echo "Cleaning build directory..."
	rm -rf $(BUILD_DIR)
