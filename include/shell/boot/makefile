# Compiler and Flags
CC      := gcc
CFLAGS  := -Wall -Wextra -O2

# Query static compiler flags and libraries using pkg-config
PKG_CFLAGS := $(shell pkg-config --static --cflags sdl2 SDL2_image)
PKG_LIBS   := $(shell pkg-config --static --libs sdl2 SDL2_image)

# Additional low-level system libraries required for static SDL2/PNG linking
EXTRA_LIBS := -lpng -lz -lm -lpthread -ldl

# Combine all libraries
LIBS := $(PKG_LIBS) $(EXTRA_LIBS)

# Target executable name
TARGET := viewer
SRC    := main.c

.PHONY: all clean check

# Default target
all: $(TARGET)

# Compile and statically link the binary
$(TARGET): $(SRC)
	$(CC) $(CFLAGS) $(PKG_CFLAGS) $< -o $@ $(LIBS)

# Check if the generated executable is truly statically linked
check: $(TARGET)
	@file $(TARGET)
	@echo "--- Dynamic Library Dependencies (should show 'not a dynamic executable') ---"
	@-ldd $(TARGET) || true

# Clean up built artifacts
clean:
	rm -f $(TARGET)
