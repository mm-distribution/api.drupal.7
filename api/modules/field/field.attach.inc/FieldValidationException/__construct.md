# FieldValidationException::__construct()

- **Type:** Method
- **File:** [`modules/field/field.attach.inc`](../_file.md), lines 26–29 · [local source](../../../../../source/modules/field/field.attach.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.attach.inc#L26-L29)
- **Class:** [FieldValidationException](../FieldValidationException.md)
- **Module/theme:** field

## Signature

```php
function __construct($errors)
```

## Documentation

```text
Constructor for FieldValidationException.

@param $errors
  An array of field validation errors, keyed by field name and
  delta that contains two keys:
  - 'error': A machine-readable error code string, prefixed by
    the field module name. A field widget may use this code to decide
    how to report the error.
  - 'message': A human-readable error message such as to be
    passed to form_error() for the appropriate form element.
```

## Code

```php
  function __construct($errors) {
    $this->errors = $errors;
    parent::__construct(t('Field validation errors'));
  }
```

---
_Drupal 7.103 · [modules/field/field.attach.inc](https://github.com/drupal/drupal/blob/7.103/modules/field/field.attach.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
