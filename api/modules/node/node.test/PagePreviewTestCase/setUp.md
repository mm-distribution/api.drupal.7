# PagePreviewTestCase::setUp()

- **Type:** Method
- **File:** [`modules/node/node.test`](../_file.md), lines 465–530 · [local source](../../../../../source/modules/node/node.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test#L465-L530)
- **Class:** [PagePreviewTestCase](../PagePreviewTestCase.md)
- **Module/theme:** node

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    parent::setUp(array('taxonomy', 'node'));

    $web_user = $this->drupalCreateUser(array('edit own page content', 'create page content'));
    $this->drupalLogin($web_user);

    // Add a vocabulary so we can test different view modes.
    $vocabulary = (object) array(
      'name' => $this->randomName(),
      'description' => $this->randomName(),
      'machine_name' => drupal_strtolower($this->randomName()),
      'help' => '',
      'nodes' => array('page' => 'page'),
    );
    taxonomy_vocabulary_save($vocabulary);

    $this->vocabulary = $vocabulary;

    // Add a term to the vocabulary.
    $term = (object) array(
      'name' => $this->randomName(),
      'description' => $this->randomName(),
      // Use the first available text format.
      'format' => db_query_range('SELECT format FROM {filter_format}', 0, 1)->fetchField(),
      'vid' => $this->vocabulary->vid,
      'vocabulary_machine_name' => $vocabulary->machine_name,
    );
    taxonomy_term_save($term);

    $this->term = $term;

    // Set up a field and instance.
    $this->field_name = drupal_strtolower($this->randomName());
    $this->field = array(
      'field_name' => $this->field_name,
      'type' => 'taxonomy_term_reference',
      'settings' => array(
        'allowed_values' => array(
          array(
            'vocabulary' => $this->vocabulary->machine_name,
            'parent' => '0',
          ),
        ),
      )
    );

    field_create_field($this->field);
    $this->instance = array(
      'field_name' => $this->field_name,
      'entity_type' => 'node',
      'bundle' => 'page',
      'widget' => array(
        'type' => 'options_select',
      ),
      // Hide on full display but render on teaser.
      'display' => array(
        'default' => array(
          'type' => 'hidden',
        ),
        'teaser' => array(
          'type' => 'taxonomy_term_reference_link',
        ),
      ),
    );
    field_create_instance($this->instance);
  }
```

---
_Drupal 7.103 · [modules/node/node.test](https://github.com/drupal/drupal/blob/7.103/modules/node/node.test) · Licensed GPL-2.0-or-later (see LICENSE)._
