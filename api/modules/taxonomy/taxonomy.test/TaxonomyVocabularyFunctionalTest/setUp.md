# TaxonomyVocabularyFunctionalTest::setUp()

- **Type:** Method
- **File:** [`modules/taxonomy/taxonomy.test`](../_file.md), lines 60–65 · [local source](../../../../../source/modules/taxonomy/taxonomy.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test#L60-L65)
- **Class:** [TaxonomyVocabularyFunctionalTest](../TaxonomyVocabularyFunctionalTest.md)
- **Module/theme:** taxonomy

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    parent::setUp();
    $this->admin_user = $this->drupalCreateUser(array('administer taxonomy'));
    $this->drupalLogin($this->admin_user);
    $this->vocabulary = $this->createVocabulary();
  }
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.test](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test) · Licensed GPL-2.0-or-later (see LICENSE)._
