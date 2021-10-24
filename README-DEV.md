### KeyboardLayoutBase class

- ASCII_TO_KEYCODE is a bytes string with the keycode for each low-ascii character at the ascii value place. The keycode for "u" is at: `ASCII_TO_KEYCODE[ord("u")]`. Since the keycode value is below 0x80, the high bit is used to encode if the shift key is needed.
- `NEED_ALTGR` lists characters that require the altgr key in addition.
- `HIGHER_ASCII` is a dictionary that associates the `ord()` int value of high ascii and utf8 characters of one or more bytes to the keycode.
- `COMBINED_KEYS` is a table (dictionary) of characters like `Ñ` that can be accessed by typing first a dead key (like `~`) followed by a regular key (like `N`) - on a Windows French keyboard for example.
  - Indexes are `ord()` int values of each character.
  - The value is an int encoding 2 bytes.
  - The upper byte is the keycode of the first key, including the shift bit.
  - The lower byte is the ascii code of the second key (a-z, A-Z or space).
  - The lower byte's high bit also encodes whether or not the first key needs altgr, so as not to pack NEEDS_ALTGR with a bunch of characters.

With the `Ñ` example:
- `~` is altgr + `é`, `é` is keycode 0x1F
- `N` is ascii code 0x4E, with the altgr bit becomes 0xCE
- `Ñ` is therefore `0xD1: 0x1FCE,`
- When typing, "N" is looked up: `ASCII_TO_KEYCODE[0x4E] == 0x91` (shift+0x11)
- So `write("Ñ")` sends the keycodes: `(0xE6, 0x1F)` (altgr+é) then `(0xE1, 0x11)` (shift+n)

Using int values to index the dictionaries, and as values for the `COMBINED_KEYS` table reduces the memory size compared to strings and bytestrings.

### Layouts and KeyboardLayout classes

Every layout class is called KeyboardLayout, to make changing layout easier without having a different class name in every file, and have to guess or lookup the class name (is it CamelCase of the module name ? Is it US or Us ?). For compatibility, I added `KeyboardLayout = KeyboardLayoutUS` in the US keyboard layout. Importing multiple layouts is possible by using the full `module.KeyboardLayout` name, or `import KeyboardLayout as ...`
