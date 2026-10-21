# TaxonomyWebTestCase::createVocabulary()

- **Type:** Method
- **File:** [`modules/taxonomy/taxonomy.test`](../_file.md), lines 16–27 · [local source](../../../../../source/modules/taxonomy/taxonomy.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test#L16-L27)
- **Class:** [TaxonomyWebTestCase](../TaxonomyWebTestCase.md)
- **Module/theme:** taxonomy

## Signature

```php
function createVocabulary()
```

## Documentation

```text
Returns a new vocabulary with random properties.
```

## Code

```php
  function createVocabulary() {
    // Create a vocabulary.
    $vocabulary = new stdClass();
    $vocabulary->name = $this->randomName();
    $vocabulary->description = $this->randomName();
    $vocabulary->machine_name = drupal_strtolower($this->randomName());
    $vocabulary->help = '';
    $vocabulary->nodes = array('article' => 'article');
    $vocabulary->weight = mt_rand(0, 10);
    taxonomy_vocabulary_save($vocabulary);
    return $vocabulary;
  }
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.test](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test) · Licensed GPL-2.0-or-later (see LICENSE)._
