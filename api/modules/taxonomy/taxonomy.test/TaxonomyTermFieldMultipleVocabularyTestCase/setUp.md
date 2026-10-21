# TaxonomyTermFieldMultipleVocabularyTestCase::setUp()

- **Type:** Method
- **File:** [`modules/taxonomy/taxonomy.test`](../_file.md), lines 1731–1773 · [local source](../../../../../source/modules/taxonomy/taxonomy.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test#L1731-L1773)
- **Class:** [TaxonomyTermFieldMultipleVocabularyTestCase](../TaxonomyTermFieldMultipleVocabularyTestCase.md)
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
    parent::setUp('field_test');

    $web_user = $this->drupalCreateUser(array('access field_test content', 'administer field_test content', 'administer taxonomy'));
    $this->drupalLogin($web_user);
    $this->vocabulary1 = $this->createVocabulary();
    $this->vocabulary2 = $this->createVocabulary();

    // Set up a field and instance.
    $this->field_name = drupal_strtolower($this->randomName());
    $this->field = array(
      'field_name' => $this->field_name,
      'type' => 'taxonomy_term_reference',
      'cardinality' => FIELD_CARDINALITY_UNLIMITED,
      'settings' => array(
        'allowed_values' => array(
          array(
            'vocabulary' => $this->vocabulary1->machine_name,
            'parent' => '0',
          ),
          array(
            'vocabulary' => $this->vocabulary2->machine_name,
            'parent' => '0',
          ),
        ),
      )
    );
    field_create_field($this->field);
    $this->instance = array(
      'field_name' => $this->field_name,
      'entity_type' => 'test_entity',
      'bundle' => 'test_bundle',
      'widget' => array(
        'type' => 'options_select',
      ),
      'display' => array(
        'full' => array(
          'type' => 'taxonomy_term_reference_link',
        ),
      ),
    );
    field_create_instance($this->instance);
  }
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.test](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test) · Licensed GPL-2.0-or-later (see LICENSE)._
