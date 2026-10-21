# hook_image_styles_alter()

- **Type:** Hook (documentation function)
- **File:** [`modules/image/image.api.php`](_file.md), lines 142–153 · [local source](../../../../source/modules/image/image.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.api.php#L142-L153)
- **Module/theme:** image
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_image_styles_alter(&$styles)
```

## Documentation

```text
Modify any image styles provided by other modules or the user.

This hook allows modules to modify, add, or remove image styles. This may
be useful to modify default styles provided by other modules or enforce
that a specific effect is always enabled on a style. Note that modifications
to these styles may negatively affect the user experience, such as if an
effect is added to a style through this hook, the user may attempt to remove
the effect but it will be immediately be re-added.

The best use of this hook is usually to modify default styles, which are not
editable by the user until they are overridden, so such interface
contradictions will not occur. This hook can target default (or user) styles
by checking the $style['storage'] property.

If your module needs to provide a new style (rather than modify an existing
one) use hook_image_default_styles() instead.

@see hook_image_default_styles()
```

## Code

```php
function hook_image_styles_alter(&$styles) {
  // Check that we only affect a default style.
  if ($styles['thumbnail']['storage'] == IMAGE_STORAGE_DEFAULT) {
    // Add an additional effect to the thumbnail style.
    $styles['thumbnail']['effects'][] = array(
      'name' => 'image_desaturate',
      'data' => array(),
      'weight' => 1,
      'effect callback' => 'image_desaturate_effect',
    );
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_image_styles_alter()".

_None found._

---
_Drupal 7.103 · [modules/image/image.api.php](https://github.com/drupal/drupal/blob/7.103/modules/image/image.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
