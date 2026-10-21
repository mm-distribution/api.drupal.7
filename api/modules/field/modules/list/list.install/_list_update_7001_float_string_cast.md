# _list_update_7001_float_string_cast()

- **Type:** Function
- **File:** [`modules/field/modules/list/list.install`](_file.md), lines 94–96 · [local source](../../../../../../source/modules/field/modules/list/list.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/list/list.install#L94-L96)
- **Module/theme:** list

## Signature

```php
function _list_update_7001_float_string_cast($element)
```

## Documentation

```text
Helper callback function to cast the array element.
```

## Code

```php
function _list_update_7001_float_string_cast($element) {
  return (string) (float) $element;
}
```

---
_Drupal 7.103 · [modules/field/modules/list/list.install](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/list/list.install) · Licensed GPL-2.0-or-later (see LICENSE)._
