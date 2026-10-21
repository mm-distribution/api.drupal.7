# taxonomy_overview_vocabularies()

- **Type:** Function
- **File:** [`modules/taxonomy/taxonomy.admin.inc`](_file.md), lines 15–43 · [local source](../../../../source/modules/taxonomy/taxonomy.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.admin.inc#L15-L43)
- **Module/theme:** taxonomy
- **Topics:** [forms](../../../topics/forms.md)

## Signature

```php
function taxonomy_overview_vocabularies($form)
```

## Documentation

```text
Form builder to list and manage vocabularies.

@ingroup forms
@see taxonomy_overview_vocabularies_submit()
@see theme_taxonomy_overview_vocabularies()
```

## Code

```php
function taxonomy_overview_vocabularies($form) {
  $vocabularies = taxonomy_get_vocabularies();
  $form['#tree'] = TRUE;
  foreach ($vocabularies as $vocabulary) {
    $form[$vocabulary->vid]['#vocabulary'] = $vocabulary;
    $form[$vocabulary->vid]['name'] = array('#markup' => check_plain($vocabulary->name));
    $form[$vocabulary->vid]['weight'] = array(
      '#type' => 'weight',
      '#title' => t('Weight for @title', array('@title' => $vocabulary->name)),
      '#title_display' => 'invisible',
      '#delta' => 10,
      '#default_value' => $vocabulary->weight,
    );
    $form[$vocabulary->vid]['edit'] = array('#type' => 'link', '#title' => t('edit vocabulary'), '#href' => "admin/structure/taxonomy/$vocabulary->machine_name/edit");
    $form[$vocabulary->vid]['list'] = array('#type' => 'link', '#title' => t('list terms'), '#href' => "admin/structure/taxonomy/$vocabulary->machine_name");
    $form[$vocabulary->vid]['add'] = array('#type' => 'link', '#title' => t('add terms'), '#href' => "admin/structure/taxonomy/$vocabulary->machine_name/add");
  }

  // Only make this form include a submit button and weight if more than one
  // vocabulary exists.
  if (count($vocabularies) > 1) {
    $form['actions'] = array('#type' => 'actions');
    $form['actions']['submit'] = array('#type' => 'submit', '#value' => t('Save'));
  }
  elseif (isset($vocabulary)) {
    unset($form[$vocabulary->vid]['weight']);
  }
  return $form;
}
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
