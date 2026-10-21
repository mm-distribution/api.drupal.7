# FileTaxonomyTermTestCase

- **Type:** Class
- **File:** [`modules/file/tests/file.test`](_file.md), lines 250–367 · [local source](../../../../../source/modules/file/tests/file.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test#L250-L367)
- **Module/theme:** file_module_test

## Signature

```php
class FileTaxonomyTermTestCase extends DrupalWebTestCase
```

## Documentation

```text
Tests adding a file to a non-node entity.
```

## Properties

### $admin_user

```php
protected $admin_user;
```

## Methods (derived index)

- [getInfo()](FileTaxonomyTermTestCase/getInfo.md)
- [setUp()](FileTaxonomyTermTestCase/setUp.md)
- [createAttachFileField()](FileTaxonomyTermTestCase/createAttachFileField.md) — Creates a file field and attaches it to the "Tags" taxonomy vocabulary.
- [testTermFilePublic()](FileTaxonomyTermTestCase/testTermFilePublic.md) — Tests that a public file can be attached to a taxonomy term.
- [testTermFilePrivate()](FileTaxonomyTermTestCase/testTermFilePrivate.md) — Tests that a private file can be attached to a taxonomy term.
- [_testTermFile()](FileTaxonomyTermTestCase/_testTermFile.md) — Runs tests for attaching a file field to a taxonomy term.

---
_Drupal 7.103 · [modules/file/tests/file.test](https://github.com/drupal/drupal/blob/7.103/modules/file/tests/file.test) · Licensed GPL-2.0-or-later (see LICENSE)._
