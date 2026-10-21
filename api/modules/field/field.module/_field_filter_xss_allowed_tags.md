# _field_filter_xss_allowed_tags()

- **Type:** Function
- **File:** [`modules/field/field.module`](_file.md), lines 763–765 · [local source](../../../../source/modules/field/field.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.module#L763-L765)
- **Module/theme:** field
- **Topics:** [field](../../../topics/field.md)

## Signature

```php
function _field_filter_xss_allowed_tags()
```

## Documentation

```text
List of tags allowed by field_filter_xss().
```

## Code

```php
function _field_filter_xss_allowed_tags() {
  return array('a', 'b', 'big',  'code', 'del', 'em', 'i', 'ins',  'pre', 'q', 'small', 'span', 'strong', 'sub', 'sup', 'tt', 'ol', 'ul', 'li', 'p', 'br', 'img');
}
```

---
_Drupal 7.103 · [modules/field/field.module](https://github.com/drupal/drupal/blob/7.103/modules/field/field.module) · Licensed GPL-2.0-or-later (see LICENSE)._
