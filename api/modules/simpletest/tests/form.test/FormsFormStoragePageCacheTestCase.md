# FormsFormStoragePageCacheTestCase

- **Type:** Class
- **File:** [`modules/simpletest/tests/form.test`](_file.md), lines 1452–1547 · [local source](../../../../../source/modules/simpletest/tests/form.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test#L1452-L1547)
- **Module/theme:** batch_test

## Signature

```php
class FormsFormStoragePageCacheTestCase extends DrupalWebTestCase
```

## Documentation

```text
Test the form storage when page caching for anonymous users is turned on.
```

## Properties

### $profile

```php
protected $profile = 'testing';
```

## Methods (derived index)

- [getInfo()](FormsFormStoragePageCacheTestCase/getInfo.md)
- [setUp()](FormsFormStoragePageCacheTestCase/setUp.md)
- [getFormBuildId()](FormsFormStoragePageCacheTestCase/getFormBuildId.md) — Return the build id of the current form.
- [testValidateFormStorageOnCachedPage()](FormsFormStoragePageCacheTestCase/testValidateFormStorageOnCachedPage.md) — Build-id is regenerated when validating cached form.
- [testRebuildFormStorageOnCachedPage()](FormsFormStoragePageCacheTestCase/testRebuildFormStorageOnCachedPage.md) — Build-id is regenerated when rebuilding cached form.

---
_Drupal 7.103 · [modules/simpletest/tests/form.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/form.test) · Licensed GPL-2.0-or-later (see LICENSE)._
