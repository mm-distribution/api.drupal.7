# Image toolkits

- **Topic id:** `image`
- **Defined in:** [`includes/image.inc`](../includes/image.inc/_file.md), line 8 · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/image.inc#L8)

## Documentation

```text
@defgroup image Image toolkits
@{
Functions for image file manipulations.

Drupal's image toolkits provide an abstraction layer for common image file
manipulations like scaling, cropping, and rotating. The abstraction frees
module authors from the need to support multiple image libraries, and it
allows site administrators to choose the library that's best for them.

PHP includes the GD library by default so a GD toolkit is installed with
Drupal. Other toolkits like ImageMagick are available from contrib modules.
GD works well for small images, but using it with larger files may cause PHP
to run out of memory. In contrast the ImageMagick library does not suffer
from this problem, but it requires the ISP to have installed additional
software.

Image toolkits are discovered based on the associated module's
hook_image_toolkits. Additionally the image toolkit include file
must be identified in the files array in the module.info file. The
toolkit must then be enabled using the admin/config/media/image-toolkit
form.

Only one toolkit may be selected at a time. If a module author wishes to call
a specific toolkit they can check that it is installed by calling
image_get_available_toolkits(), and then calling its functions directly.
```

## Members (derived, 24)

From `@ingroup` tags and `@addtogroup`/`@defgroup` `@{ … @}` regions in the source.

- [image_crop()](../includes/image.inc/image_crop.md) (function) — Crops an image to a rectangle specified by the given dimensions.
- [image_desaturate()](../includes/image.inc/image_desaturate.md) (function) — Converts an image to grayscale.
- [image_dimensions_scale()](../includes/image.inc/image_dimensions_scale.md) (function) — Scales image dimensions while maintaining aspect ratio.
- [image_gd_check_settings()](../modules/system/image.gd.inc/image_gd_check_settings.md) (function) — Verify GD2 settings (that the right version is actually installed).
- [image_gd_create_tmp()](../modules/system/image.gd.inc/image_gd_create_tmp.md) (function) — Create a truecolor image preserving transparency from a provided image.
- [image_gd_crop()](../modules/system/image.gd.inc/image_gd_crop.md) (function) — Crop an image using the GD toolkit.
- [image_gd_desaturate()](../modules/system/image.gd.inc/image_gd_desaturate.md) (function) — Convert an image resource to grayscale.
- [image_gd_get_info()](../modules/system/image.gd.inc/image_gd_get_info.md) (function) — Get details about an image.
- [image_gd_load()](../modules/system/image.gd.inc/image_gd_load.md) (function) — GD helper function to create an image resource from a file.
- [image_gd_resize()](../modules/system/image.gd.inc/image_gd_resize.md) (function) — Scale an image to the specified size using GD.
- [image_gd_rotate()](../modules/system/image.gd.inc/image_gd_rotate.md) (function) — Rotate an image the given number of degrees.
- [image_gd_save()](../modules/system/image.gd.inc/image_gd_save.md) (function) — GD helper to write an image resource to a destination file.
- [image_gd_settings()](../modules/system/image.gd.inc/image_gd_settings.md) (function) — Retrieve settings for the GD2 toolkit.
- [image_gd_settings_validate()](../modules/system/image.gd.inc/image_gd_settings_validate.md) (function) — Validate the submitted GD settings.
- [image_get_available_toolkits()](../includes/image.inc/image_get_available_toolkits.md) (function) — Gets a list of available toolkits.
- [image_get_info()](../includes/image.inc/image_get_info.md) (function) — Gets details about an image.
- [image_get_toolkit()](../includes/image.inc/image_get_toolkit.md) (function) — Gets the name of the currently used toolkit.
- [image_load()](../includes/image.inc/image_load.md) (function) — Loads an image file and returns an image object.
- [image_resize()](../includes/image.inc/image_resize.md) (function) — Resizes an image to the given dimensions (ignoring aspect ratio).
- [image_rotate()](../includes/image.inc/image_rotate.md) (function) — Rotates an image by the given number of degrees.
- [image_save()](../includes/image.inc/image_save.md) (function) — Closes the image and saves the changes to a file.
- [image_scale()](../includes/image.inc/image_scale.md) (function) — Scales an image while maintaining aspect ratio.
- [image_scale_and_crop()](../includes/image.inc/image_scale_and_crop.md) (function) — Scales an image to the exact width and height given.
- [image_toolkit_invoke()](../includes/image.inc/image_toolkit_invoke.md) (function) — Invokes the given method using the currently selected toolkit.

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
