# FieldTranslationsTestCase

- **Type:** Class
- **File:** [`modules/field/tests/field.test`](_file.md), lines 3152–3501 · [local source](../../../../../source/modules/field/tests/field.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test#L3152-L3501)
- **Module/theme:** field_test_schema_alter

## Signature

```php
class FieldTranslationsTestCase extends FieldTestCase
```

## Documentation

```text
Unit test class for the multilanguage fields logic.

The following tests will check the multilanguage logic of _field_invoke() and
that only the correct values are returned by field_available_languages().
```

## Properties

### $field

```php
protected $field;
```

### $instance

```php
protected $instance;
```

### $field_name

```php
protected $field_name;
```

### $entity_type

```php
protected $entity_type;
```

## Methods (derived index)

- [getInfo()](FieldTranslationsTestCase/getInfo.md)
- [setUp()](FieldTranslationsTestCase/setUp.md)
- [testFieldAvailableLanguages()](FieldTranslationsTestCase/testFieldAvailableLanguages.md) — Ensures that only valid values are returned by field_available_languages().
- [testFieldInvoke()](FieldTranslationsTestCase/testFieldInvoke.md) — Test the multilanguage logic of _field_invoke().
- [testFieldInvokeMultiple()](FieldTranslationsTestCase/testFieldInvokeMultiple.md) — Test the multilanguage logic of _field_invoke_multiple().
- [testTranslatableFieldSaveLoad()](FieldTranslationsTestCase/testTranslatableFieldSaveLoad.md) — Test translatable fields storage/retrieval.
- [testFieldDisplayLanguage()](FieldTranslationsTestCase/testFieldDisplayLanguage.md) — Tests display language logic for translatable fields.
- [testFieldFormTranslationRevisions()](FieldTranslationsTestCase/testFieldFormTranslationRevisions.md) — Tests field translations when creating a new revision.
- [checkTranslationRevisions()](FieldTranslationsTestCase/checkTranslationRevisions.md) — Check if the field translation attached to the entity revision identified by the passed arguments were correctly stored.

---
_Drupal 7.103 · [modules/field/tests/field.test](https://github.com/drupal/drupal/blob/7.103/modules/field/tests/field.test) · Licensed GPL-2.0-or-later (see LICENSE)._
