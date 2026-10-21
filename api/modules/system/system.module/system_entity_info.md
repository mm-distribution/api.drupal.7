# system_entity_info()

- **Type:** Function
- **File:** [`modules/system/system.module`](_file.md), lines 281–293 · [local source](../../../../source/modules/system/system.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module#L281-L293)
- **Module/theme:** system
- **Implements:** [hook_entity_info()](../system.api.php/hook_entity_info.md)

## Signature

```php
function system_entity_info()
```

## Documentation

```text
Implements hook_entity_info().
```

## Code

```php
function system_entity_info() {
  return array(
    'file' => array(
      'label' => t('File'),
      'base table' => 'file_managed',
      'entity keys' => array(
        'id' => 'fid',
        'label' => 'filename',
      ),
      'static cache' => FALSE,
    ),
  );
}
```

---
_Drupal 7.103 · [modules/system/system.module](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module) · Licensed GPL-2.0-or-later (see LICENSE)._
