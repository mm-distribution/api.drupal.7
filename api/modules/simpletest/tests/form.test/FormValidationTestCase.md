# FormValidationTestCase

- **Type:** Class
- **File:** [`modules/simpletest/tests/form.test`](_file.md), lines 646–769 · [local source](../../../../../source/modules/simpletest/tests/form.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test#L646-L769)
- **Module/theme:** batch_test

## Signature

```php
class FormValidationTestCase extends DrupalWebTestCase
```

## Documentation

```text
Test form validation handlers.
```

## Methods (derived index)

- [getInfo()](FormValidationTestCase/getInfo.md)
- [setUp()](FormValidationTestCase/setUp.md)
- [testValidate()](FormValidationTestCase/testValidate.md) — Tests form alterations by #element_validate, #validate, and form_set_value().
- [testDisabledToken()](FormValidationTestCase/testDisabledToken.md) — Tests that a form with a disabled CSRF token can be validated.
- [testValidateLimitErrors()](FormValidationTestCase/testValidateLimitErrors.md) — Tests partial form validation through #limit_validation_errors.
- [testMultiFormSameNameErrorClass()](FormValidationTestCase/testMultiFormSameNameErrorClass.md) — Tests error border of multiple fields with same name in a page.

---
_Drupal 7.103 · [modules/simpletest/tests/form.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test) · Licensed GPL-2.0-or-later (see LICENSE)._
