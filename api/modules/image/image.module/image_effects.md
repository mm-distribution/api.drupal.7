# image_effects()

- **Type:** Function
- **File:** [`modules/image/image.module`](_file.md), lines 1318–1341 · [local source](../../../../source/modules/image/image.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.module#L1318-L1341)
- **Module/theme:** image

## Signature

```php
function image_effects()
```

## Documentation

```text
Loads all image effects from the database.

@return
  An array of all image effects.
@see image_effect_load()
```

## Code

```php
function image_effects() {
  $effects = &drupal_static(__FUNCTION__);

  if (!isset($effects)) {
    $effects = array();

    // Add database image effects.
    $result = db_select('image_effects', NULL, array('fetch' => PDO::FETCH_ASSOC))
      ->fields('image_effects')
      ->orderBy('image_effects.weight', 'ASC')
      ->execute();
    foreach ($result as $effect) {
      $effect['data'] = unserialize($effect['data']);
      $definition = image_effect_definition_load($effect['name']);
      // Do not load image effects whose definition cannot be found.
      if ($definition) {
        $effect = array_merge($definition, $effect);
        $effects[$effect['ieid']] = $effect;
      }
    }
  }

  return $effects;
}
```

---
_Drupal 7.103 · [modules/image/image.module](https://github.com/drupal/drupal/blob/7.103/modules/image/image.module) · Licensed GPL-2.0-or-later (see LICENSE)._
