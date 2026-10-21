# image_effect_scale_validate()

- **Type:** Function
- **File:** [`modules/image/image.admin.inc`](_file.md), lines 522–526 · [local source](../../../../source/modules/image/image.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.admin.inc#L522-L526)
- **Module/theme:** image

## Signature

```php
function image_effect_scale_validate($element, &$form_state)
```

## Documentation

```text
Element validate handler to ensure that either a height or a width is
specified.
```

## Code

```php
function image_effect_scale_validate($element, &$form_state) {
  if (empty($element['width']['#value']) && empty($element['height']['#value'])) {
    form_error($element, t('Width and height can not both be blank.'));
  }
}
```

---
_Drupal 7.103 · [modules/image/image.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/image/image.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
