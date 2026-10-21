# image_effect_definitions()

- **Type:** Function
- **File:** [`modules/image/image.module`](_file.md), lines 1237–1269 · [local source](../../../../source/modules/image/image.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.module#L1237-L1269)
- **Module/theme:** image

## Signature

```php
function image_effect_definitions()
```

## Documentation

```text
Returns a set of image effects.

These image effects are exposed by modules implementing
hook_image_effect_info().

@return
  An array of image effects to be used when transforming images.
@see hook_image_effect_info()
@see image_effect_definition_load()
```

## Code

```php
function image_effect_definitions() {
  global $language;

  // hook_image_effect_info() includes translated strings, so each language is
  // cached separately.
  $langcode = $language->language;

  $effects = &drupal_static(__FUNCTION__);

  if (!isset($effects)) {
    if ($cache = cache_get("image_effects:$langcode")) {
      $effects = $cache->data;
    }
    else {
      $effects = array();
      include_once DRUPAL_ROOT . '/modules/image/image.effects.inc';
      foreach (module_implements('image_effect_info') as $module) {
        foreach (module_invoke($module, 'image_effect_info') as $name => $effect) {
          // Ensure the current toolkit supports the effect.
          $effect['module'] = $module;
          $effect['name'] = $name;
          $effect['data'] = isset($effect['data']) ? $effect['data'] : array();
          $effects[$name] = $effect;
        }
      }
      uasort($effects, '_image_effect_definitions_sort');
      drupal_alter('image_effect_info', $effects);
      cache_set("image_effects:$langcode", $effects);
    }
  }

  return $effects;
}
```

---
_Drupal 7.103 · [modules/image/image.module](https://github.com/drupal/drupal/blob/7.103/modules/image/image.module) · Licensed GPL-2.0-or-later (see LICENSE)._
