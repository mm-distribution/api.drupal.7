# forum_enable()

- **Type:** Function
- **File:** [`modules/forum/forum.install`](_file.md), lines 25–100 · [local source](../../../../source/modules/forum/forum.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.install#L25-L100)
- **Module/theme:** forum
- **Implements:** [hook_enable()](../../system/system.api.php/hook_enable.md)

## Signature

```php
function forum_enable()
```

## Documentation

```text
Implements hook_enable().
```

## Code

```php
function forum_enable() {
  // If we enable forum at the same time as taxonomy we need to call
  // field_associate_fields() as otherwise the field won't be enabled until
  // hook modules_enabled is called which takes place after hook_enable events.
  field_associate_fields('taxonomy');
  // Create the forum vocabulary if it does not exist.
  $vocabulary = taxonomy_vocabulary_load(variable_get('forum_nav_vocabulary', 0));
  if (!$vocabulary) {
    $edit = array(
      'name' => t('Forums'),
      'machine_name' => 'forums',
      'description' => t('Forum navigation vocabulary'),
      'hierarchy' => 1,
      'module' => 'forum',
      'weight' => -10,
    );
    $vocabulary = (object) $edit;
    taxonomy_vocabulary_save($vocabulary);
    variable_set('forum_nav_vocabulary', $vocabulary->vid);
  }

  // Create the 'taxonomy_forums' field if it doesn't already exist.
  if (!field_info_field('taxonomy_forums')) {
    $field = array(
      'field_name' => 'taxonomy_forums',
      'type' => 'taxonomy_term_reference',
      'settings' => array(
        'allowed_values' => array(
          array(
            'vocabulary' => $vocabulary->machine_name,
            'parent' => 0,
          ),
        ),
      ),
    );
    field_create_field($field);

    // Create a default forum so forum posts can be created.
    $edit = array(
      'name' => t('General discussion'),
      'description' => '',
      'parent' => array(0),
      'vid' => $vocabulary->vid,
    );
    $term = (object) $edit;
    taxonomy_term_save($term);

    // Create the instance on the bundle.
    $instance = array(
      'field_name' => 'taxonomy_forums',
      'entity_type' => 'node',
      'label' => $vocabulary->name,
      'bundle' => 'forum',
      'required' => TRUE,
      'widget' => array(
        'type' => 'options_select',
      ),
      'display' => array(
        'default' => array(
          'type' => 'taxonomy_term_reference_link',
         'weight' => 10,
        ),
        'teaser' => array(
          'type' => 'taxonomy_term_reference_link',
         'weight' => 10,
        ),
      ),
    );
    field_create_instance($instance);
  }

  // Ensure the forum node type is available.
  node_types_rebuild();
  $types = node_type_get_types();
  node_add_body_field($types['forum']);
}
```

---
_Drupal 7.103 · [modules/forum/forum.install](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.install) · Licensed GPL-2.0-or-later (see LICENSE)._
