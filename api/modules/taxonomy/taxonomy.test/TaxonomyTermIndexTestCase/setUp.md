# TaxonomyTermIndexTestCase::setUp()

- **Type:** Method
- **File:** [`modules/taxonomy/taxonomy.test`](../_file.md), lines 1192–1261 · [local source](../../../../../source/modules/taxonomy/taxonomy.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test#L1192-L1261)
- **Class:** [TaxonomyTermIndexTestCase](../TaxonomyTermIndexTestCase.md)
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
    parent::setUp('taxonomy');

    // Create an administrative user.
    $this->admin_user = $this->drupalCreateUser(array('administer taxonomy', 'bypass node access'));
    $this->drupalLogin($this->admin_user);

    // Create a vocabulary and add two term reference fields to article nodes.
    $this->vocabulary = $this->createVocabulary();

    $this->field_name_1 = drupal_strtolower($this->randomName());
    $this->field_1 = array(
      'field_name' => $this->field_name_1,
      'type' => 'taxonomy_term_reference',
      'cardinality' => FIELD_CARDINALITY_UNLIMITED,
      'settings' => array(
        'allowed_values' => array(
          array(
            'vocabulary' => $this->vocabulary->machine_name,
            'parent' => 0,
          ),
        ),
      ),
    );
    field_create_field($this->field_1);
    $this->instance_1 = array(
      'field_name' => $this->field_name_1,
      'bundle' => 'article',
      'entity_type' => 'node',
      'widget' => array(
        'type' => 'options_select',
      ),
      'display' => array(
        'default' => array(
          'type' => 'taxonomy_term_reference_link',
        ),
      ),
    );
    field_create_instance($this->instance_1);

    $this->field_name_2 = drupal_strtolower($this->randomName());
    $this->field_2 = array(
      'field_name' => $this->field_name_2,
      'type' => 'taxonomy_term_reference',
      'cardinality' => FIELD_CARDINALITY_UNLIMITED,
      'settings' => array(
        'allowed_values' => array(
          array(
            'vocabulary' => $this->vocabulary->machine_name,
            'parent' => 0,
          ),
        ),
      ),
    );
    field_create_field($this->field_2);
    $this->instance_2 = array(
      'field_name' => $this->field_name_2,
      'bundle' => 'article',
      'entity_type' => 'node',
      'widget' => array(
        'type' => 'options_select',
      ),
      'display' => array(
        'default' => array(
          'type' => 'taxonomy_term_reference_link',
        ),
      ),
    );
    field_create_instance($this->instance_2);
  }
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.test](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test) · Licensed GPL-2.0-or-later (see LICENSE)._
