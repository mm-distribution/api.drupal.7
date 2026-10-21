# TaxonomyPrivateFileTestCase::setUp()

- **Type:** Method
- **File:** [`modules/taxonomy/taxonomy.test`](../_file.md), lines 2274–2301 · [local source](../../../../../source/modules/taxonomy/taxonomy.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test#L2274-L2301)
- **Class:** [TaxonomyPrivateFileTestCase](../TaxonomyPrivateFileTestCase.md)
- **Module/theme:** taxonomy

## Signature

```php
public function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  public function setUp() {
    parent::setUp('taxonomy_test');

    // Remove access content permission from registered users.
    user_role_revoke_permissions(DRUPAL_AUTHENTICATED_RID, array('access content'));

    $this->vocabulary = $this->createVocabulary();
    // Add a field instance to the vocabulary.
    $field = array(
      'field_name' => 'field_test',
      'type' => 'image',
      'settings' => array(
        'uri_scheme' => 'private'
      ),
    );
    field_create_field($field);
    $instance = array(
      'field_name' => 'field_test',
      'entity_type' => 'taxonomy_term',
      'label' => 'test',
      'bundle' => $this->vocabulary->machine_name,
      'widget' => array(
        'type' => 'image_image',
        'settings' => array(),
      ),
    );
    field_create_instance($instance);
  }
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.test](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.test) · Licensed GPL-2.0-or-later (see LICENSE)._
