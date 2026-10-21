# taxonomy_menu()

- **Type:** Function
- **File:** [`modules/taxonomy/taxonomy.module`](_file.md), lines 259–360 · [local source](../../../../source/modules/taxonomy/taxonomy.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module#L259-L360)
- **Module/theme:** taxonomy
- **Implements:** [hook_menu()](../../system/system.api.php/hook_menu.md)

## Signature

```php
function taxonomy_menu()
```

## Documentation

```text
Implements hook_menu().
```

## Code

```php
function taxonomy_menu() {
  $items['admin/structure/taxonomy'] = array(
    'title' => 'Taxonomy',
    'description' => 'Manage tagging, categorization, and classification of your content.',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('taxonomy_overview_vocabularies'),
    'access arguments' => array('administer taxonomy'),
    'file' => 'taxonomy.admin.inc',
  );
  $items['admin/structure/taxonomy/list'] = array(
    'title' => 'List',
    'type' => MENU_DEFAULT_LOCAL_TASK,
    'weight' => -10,
  );
  $items['admin/structure/taxonomy/add'] = array(
    'title' => 'Add vocabulary',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('taxonomy_form_vocabulary'),
    'access arguments' => array('administer taxonomy'),
    'type' => MENU_LOCAL_ACTION,
    'file' => 'taxonomy.admin.inc',
  );

  $items['taxonomy/term/%taxonomy_term'] = array(
    'title' => 'Taxonomy term',
    'title callback' => 'taxonomy_term_title',
    'title arguments' => array(2),
    // The page callback also invokes drupal_set_title() in case
    // the menu router's title is overridden by a menu link.
    'page callback' => 'taxonomy_term_page',
    'page arguments' => array(2),
    'access arguments' => array('access content'),
    'file' => 'taxonomy.pages.inc',
  );
  $items['taxonomy/term/%taxonomy_term/view'] = array(
    'title' => 'View',
    'type' => MENU_DEFAULT_LOCAL_TASK,
  );
  $items['taxonomy/term/%taxonomy_term/edit'] = array(
    'title' => 'Edit',
    'page callback' => 'drupal_get_form',
    // Pass a NULL argument to ensure that additional path components are not
    // passed to taxonomy_form_term() as the vocabulary machine name argument.
    'page arguments' => array('taxonomy_form_term', 2, NULL),
    'access callback' => 'taxonomy_term_edit_access',
    'access arguments' => array(2),
    'type' => MENU_LOCAL_TASK,
    'weight' => 10,
    'file' => 'taxonomy.admin.inc',
  );
  $items['taxonomy/term/%taxonomy_term/feed'] = array(
    'title' => 'Taxonomy term',
    'title callback' => 'taxonomy_term_title',
    'title arguments' => array(2),
    'page callback' => 'taxonomy_term_feed',
    'page arguments' => array(2),
    'access arguments' => array('access content'),
    'type' => MENU_CALLBACK,
    'file' => 'taxonomy.pages.inc',
  );
  $items['taxonomy/autocomplete'] = array(
    'title' => 'Autocomplete taxonomy',
    'page callback' => 'taxonomy_autocomplete',
    'access arguments' => array('access content'),
    'type' => MENU_CALLBACK,
    'file' => 'taxonomy.pages.inc',
  );

  $items['admin/structure/taxonomy/%taxonomy_vocabulary_machine_name'] = array(
    'title callback' => 'entity_label',
    'title arguments' => array('taxonomy_vocabulary', 3),
    'page callback' => 'drupal_get_form',
    'page arguments' => array('taxonomy_overview_terms', 3),
    'access arguments' => array('administer taxonomy'),
    'file' => 'taxonomy.admin.inc',
  );
  $items['admin/structure/taxonomy/%taxonomy_vocabulary_machine_name/list'] = array(
    'title' => 'List',
    'type' => MENU_DEFAULT_LOCAL_TASK,
    'weight' => -20,
  );
  $items['admin/structure/taxonomy/%taxonomy_vocabulary_machine_name/edit'] = array(
    'title' => 'Edit',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('taxonomy_form_vocabulary', 3),
    'access arguments' => array('administer taxonomy'),
    'type' => MENU_LOCAL_TASK,
    'weight' => -10,
    'file' => 'taxonomy.admin.inc',
  );

  $items['admin/structure/taxonomy/%taxonomy_vocabulary_machine_name/add'] = array(
    'title' => 'Add term',
    'page callback' => 'drupal_get_form',
    'page arguments' => array('taxonomy_form_term', array(), 3),
    'access arguments' => array('administer taxonomy'),
    'type' => MENU_LOCAL_ACTION,
    'file' => 'taxonomy.admin.inc',
  );

  return $items;
}
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.module](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.module) · Licensed GPL-2.0-or-later (see LICENSE)._
