# date_validate()

- **Type:** Function
- **File:** [`includes/form.inc`](_file.md), lines 3153–3157 · [local source](../../../source/includes/form.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/form.inc#L3153-L3157)
- **Topics:** [form_api](../../topics/form_api.md)

## Signature

```php
function date_validate($element)
```

## Documentation

```text
Validates the date type to prevent invalid dates (e.g., February 30, 2006).
```

## Code

```php
function date_validate($element) {
  if (!checkdate($element['#value']['month'], $element['#value']['day'], $element['#value']['year'])) {
    form_error($element, t('The specified date is invalid.'));
  }
}
```

---
_Drupal 7.103 · [includes/form.inc](https://github.com/drupal/drupal/blob/7.103/includes/form.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
