# system_file_download()

- **Type:** Function
- **File:** [`modules/system/system.module`](_file.md), lines 4109–4141 · [local source](../../../../source/modules/system/system.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module#L4109-L4141)
- **Module/theme:** system
- **Implements:** [hook_file_download()](../system.api.php/hook_file_download.md)

## Signature

```php
function system_file_download($uri)
```

## Documentation

```text
Implements hook_file_download().
```

## Code

```php
function system_file_download($uri) {
  $scheme = file_uri_scheme($uri);
  if (file_stream_wrapper_valid_scheme($scheme)) {
    $target = file_uri_target($uri);
    if ($target !== FALSE) {
      if (!in_array($scheme, variable_get('file_sa_core_2023_005_schemes', array()))) {
        if (DIRECTORY_SEPARATOR !== '/') {
          $class = file_stream_wrapper_get_class($scheme);
          if (is_subclass_of($class, 'DrupalLocalStreamWrapper')) {
            $target = str_replace(DIRECTORY_SEPARATOR, '/', $target);
          }
        }
        $parts = explode('/', $target);
        if (array_intersect($parts, array('.', '..'))) {
          return -1;
        }
      }
    }
  }

  $core_schemes = array('public', 'private', 'temporary');
  $additional_public_schemes = array_diff(variable_get('file_additional_public_schemes', array()), $core_schemes);
  if ($additional_public_schemes) {
    $scheme = file_uri_scheme($uri);
    if (in_array($scheme, $additional_public_schemes, TRUE)) {
      return array(
        // Returning any header grants access, and setting the 'Cache-Control'
        // header is appropriate for public files.
        'Cache-Control' => 'public',
      );
    }
  }
}
```

---
_Drupal 7.103 · [modules/system/system.module](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module) · Licensed GPL-2.0-or-later (see LICENSE)._
