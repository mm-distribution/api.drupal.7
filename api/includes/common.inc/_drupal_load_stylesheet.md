# _drupal_load_stylesheet()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 3947–3962 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L3947-L3962)

## Signature

```php
function _drupal_load_stylesheet($matches)
```

## Documentation

```text
Loads stylesheets recursively and returns contents with corrected paths.

This function is used for recursive loading of stylesheets and
returns the stylesheet content with all url() paths corrected.
```

## Code

```php
function _drupal_load_stylesheet($matches) {
  $filename = $matches[1];
  // Load the imported stylesheet and replace @import commands in there as well.
  $file = drupal_load_stylesheet($filename, NULL, FALSE);

  // Determine the file's directory.
  $directory = dirname($filename);
  // If the file is in the current directory, make sure '.' doesn't appear in
  // the url() path.
  $directory = $directory == '.' ? '' : $directory .'/';

  // Alter all internal url() paths. Leave external paths alone. We don't need
  // to normalize absolute paths here (i.e. remove folder/... segments) because
  // that will be done later.
  return preg_replace('/url\(\s*([\'"]?)(?![a-z]+:|\/+)([^\'")]+)([\'"]?)\s*\)/i', 'url(\1' . $directory . '\2\3)', $file);
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
