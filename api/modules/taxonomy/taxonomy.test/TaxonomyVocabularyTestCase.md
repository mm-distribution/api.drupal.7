# TaxonomyVocabularyTestCase

- **Type:** Class
- **File:** [`modules/taxonomy/taxonomy.test`](_file.md), lines 199–407 · [local source](../../../../source/modules/taxonomy/taxonomy.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test#L199-L407)
- **Module/theme:** taxonomy

## Signature

```php
class TaxonomyVocabularyTestCase extends TaxonomyWebTestCase
```

## Documentation

```text
Tests for taxonomy vocabulary functions.
```

## Properties

### $vocabulary

```php
protected $vocabulary;
```

### $field

```php
protected $field;
```

### $field_name

```php
protected $field_name;
```

### $instance

```php
protected $instance;
```

## Methods (derived index)

- [getInfo()](TaxonomyVocabularyTestCase/getInfo.md)
- [setUp()](TaxonomyVocabularyTestCase/setUp.md)
- [testTaxonomyVocabularyLoadReturnFalse()](TaxonomyVocabularyTestCase/testTaxonomyVocabularyLoadReturnFalse.md) — Ensure that when an invalid vocabulary vid is loaded, it is possible to load the same vid successfully if it subsequently becomes valid.
- [testTaxonomyVocabularyDeleteWithTerms()](TaxonomyVocabularyTestCase/testTaxonomyVocabularyDeleteWithTerms.md) — Test deleting a taxonomy that contains terms.
- [testTaxonomyVocabularyLoadStaticReset()](TaxonomyVocabularyTestCase/testTaxonomyVocabularyLoadStaticReset.md) — Ensure that the vocabulary static reset works correctly.
- [testTaxonomyVocabularyLoadMultiple()](TaxonomyVocabularyTestCase/testTaxonomyVocabularyLoadMultiple.md) — Tests for loading multiple vocabularies.
- [testTaxonomyVocabularyChangeMachineName()](TaxonomyVocabularyTestCase/testTaxonomyVocabularyChangeMachineName.md) — Tests that machine name changes are properly reflected.
- [testUninstallReinstall()](TaxonomyVocabularyTestCase/testUninstallReinstall.md) — Test uninstall and reinstall of the taxonomy module.

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.test](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test) · Licensed GPL-2.0-or-later (see LICENSE)._
