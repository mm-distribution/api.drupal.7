# system_stream_wrappers()

- **Type:** Function
- **File:** [`modules/system/system.module`](_file.md), lines 1682–1709 · [local source](../../../../source/modules/system/system.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module#L1682-L1709)
- **Module/theme:** system
- **Implements:** [hook_stream_wrappers()](../system.api.php/hook_stream_wrappers.md)

## Signature

```php
function system_stream_wrappers()
```

## Documentation

```text
Implements hook_stream_wrappers().
```

## Code

```php
function system_stream_wrappers() {
  $wrappers = array(
    'public' => array(
      'name' => t('Public files'),
      'class' => 'DrupalPublicStreamWrapper',
      'description' => t('Public local files served by the webserver.'),
      'type' => STREAM_WRAPPERS_LOCAL_NORMAL,
    ),
    'temporary' => array(
      'name' => t('Temporary files'),
      'class' => 'DrupalTemporaryStreamWrapper',
      'description' => t('Temporary local files for upload and previews.'),
      'type' => STREAM_WRAPPERS_LOCAL_HIDDEN,
    ),
  );

  // Only register the private file stream wrapper if a file path has been set.
  if (variable_get('file_private_path', FALSE)) {
    $wrappers['private'] = array(
      'name' => t('Private files'),
      'class' => 'DrupalPrivateStreamWrapper',
      'description' => t('Private local files served by Drupal.'),
      'type' => STREAM_WRAPPERS_LOCAL_NORMAL,
    );
  }

  return $wrappers;
}
```

---
_Drupal 7.103 · [modules/system/system.module](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module) · Licensed GPL-2.0-or-later (see LICENSE)._
