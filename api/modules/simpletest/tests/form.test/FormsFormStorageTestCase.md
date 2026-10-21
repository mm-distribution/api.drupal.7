# FormsFormStorageTestCase

- **Type:** Class
- **File:** [`modules/simpletest/tests/form.test`](_file.md), lines 1231–1447 · [local source](../../../../../source/modules/simpletest/tests/form.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test#L1231-L1447)
- **Module/theme:** batch_test

## Signature

```php
class FormsFormStorageTestCase extends DrupalWebTestCase
```

## Documentation

```text
Test the form storage on a multistep form.

The tested form puts data into the storage during the initial form
construction. These tests verify that there are no duplicate form
constructions, with and without manual form caching activiated. Furthermore
when a validation error occurs, it makes sure that changed form element
values aren't lost due to a wrong form rebuild.
```

## Properties

### $web_user

```php
protected $web_user;
```

## Methods (derived index)

- [getInfo()](FormsFormStorageTestCase/getInfo.md)
- [setUp()](FormsFormStorageTestCase/setUp.md)
- [testForm()](FormsFormStorageTestCase/testForm.md) — Tests using the form in a usual way.
- [testFormCached()](FormsFormStorageTestCase/testFormCached.md) — Tests using the form with an activated $form_state['cache'] property.
- [testValidation()](FormsFormStorageTestCase/testValidation.md) — Tests validation when form storage is used.
- [testCachedFormStorageValidation()](FormsFormStorageTestCase/testCachedFormStorageValidation.md) — Tests updating cached form storage during form validation.
- [testFormStatePersist()](FormsFormStorageTestCase/testFormStatePersist.md) — Tests a form using form state without using 'storage' to pass data from the constructor to a submit handler. The data has to persist even when caching gets activated, what may happen when a modules alter the form and adds #ajax properties.
- [testMutableForm()](FormsFormStorageTestCase/testMutableForm.md) — Verify that the form build-id remains the same when validation errors occur on a mutable form.
- [testImmutableForm()](FormsFormStorageTestCase/testImmutableForm.md) — Verifies that form build-id is regenerated when loading an immutable form from the cache.
- [testImmutableFormLegacyProtection()](FormsFormStorageTestCase/testImmutableFormLegacyProtection.md) — Verify that existing contrib code cannot overwrite immutable form state.

---
_Drupal 7.103 · [modules/simpletest/tests/form.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test) · Licensed GPL-2.0-or-later (see LICENSE)._
