# image_styles()

- **Type:** Function
- **File:** [`modules/image/image.module`](_file.md), lines 565–628 · [local source](../../../../source/modules/image/image.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.module#L565-L628)
- **Module/theme:** image

## Signature

```php
function image_styles()
```

## Documentation

```text
Gets an array of all styles and their settings.

@return
  An array of styles keyed by the image style ID (isid).
@see image_style_load()
```

## Code

```php
function image_styles() {
  $styles = &drupal_static(__FUNCTION__);

  // Grab from cache or build the array.
  if (!isset($styles)) {
    if ($cache = cache_get('image_styles', 'cache')) {
      $styles = $cache->data;
    }
    else {
      $styles = array();

      // Select the module-defined styles.
      foreach (module_implements('image_default_styles') as $module) {
        $module_styles = module_invoke($module, 'image_default_styles');
        foreach ($module_styles as $style_name => $style) {
          $style['name'] = $style_name;
          $style['label'] = empty($style['label']) ? $style_name : $style['label'];
          $style['module'] = $module;
          $style['storage'] = IMAGE_STORAGE_DEFAULT;
          foreach ($style['effects'] as $key => $effect) {
            $definition = image_effect_definition_load($effect['name']);
            if ($definition) {
              $effect = array_merge($definition, $effect);
              $style['effects'][$key] = $effect;
            }
            else {
              watchdog('image', 'Image style %style_name has an effect %effect_name with no definition.',
                array(
                  '%style_name' => $style_name,
                  '%effect_name' => $effect['name'],
                  ),
                WATCHDOG_ERROR);
            }
          }
          $styles[$style_name] = $style;
        }
      }

      // Select all the user-defined styles.
      $user_styles = db_select('image_styles', NULL, array('fetch' => PDO::FETCH_ASSOC))
        ->fields('image_styles')
        ->orderBy('name')
        ->execute()
        ->fetchAllAssoc('name', PDO::FETCH_ASSOC);

      // Allow the user styles to override the module styles.
      foreach ($user_styles as $style_name => $style) {
        $style['module'] = NULL;
        $style['storage'] = IMAGE_STORAGE_NORMAL;
        $style['effects'] = image_style_effects($style);
        if (isset($styles[$style_name]['module'])) {
          $style['module'] = $styles[$style_name]['module'];
          $style['storage'] = IMAGE_STORAGE_OVERRIDE;
        }
        $styles[$style_name] = $style;
      }

      drupal_alter('image_styles', $styles);
      cache_set('image_styles', $styles);
    }
  }

  return $styles;
}
```

---
_Drupal 7.103 · [modules/image/image.module](https://github.com/drupal/drupal/blob/7.103/modules/image/image.module) · Licensed GPL-2.0-or-later (see LICENSE)._
