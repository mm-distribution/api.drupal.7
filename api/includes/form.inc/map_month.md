# map_month()

- **Type:** Function
- **File:** [`includes/form.inc`](_file.md), lines 3162–3178 · [local source](../../../source/includes/form.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/form.inc#L3162-L3178)
- **Topics:** [form_api](../../topics/form_api.md)

## Signature

```php
function map_month($month)
```

## Documentation

```text
Helper function for usage with drupal_map_assoc to display month names.
```

## Code

```php
function map_month($month) {
  $months = &drupal_static(__FUNCTION__, array(
    1 => 'Jan',
    2 => 'Feb',
    3 => 'Mar',
    4 => 'Apr',
    5 => 'May',
    6 => 'Jun',
    7 => 'Jul',
    8 => 'Aug',
    9 => 'Sep',
    10 => 'Oct',
    11 => 'Nov',
    12 => 'Dec',
  ));
  return t($months[$month]);
}
```

---
_Drupal 7.103 · [includes/form.inc](https://github.com/drupal/drupal/blob/7.103/includes/form.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
