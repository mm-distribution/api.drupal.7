# taxonomy_form_term()

- **Type:** Function
- **File:** [`modules/taxonomy/taxonomy.admin.inc`](_file.md), lines 637–780 · [local source](../../../../source/modules/taxonomy/taxonomy.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.admin.inc#L637-L780)
- **Module/theme:** taxonomy
- **Topics:** [forms](../../../topics/forms.md)

## Signature

```php
function taxonomy_form_term($form, &$form_state, $edit = array(), $vocabulary = NULL)
```

## Documentation

```text
Form function for the term edit form.

@ingroup forms
@see taxonomy_form_term_submit()
```

## Code

```php
function taxonomy_form_term($form, &$form_state, $edit = array(), $vocabulary = NULL) {
  // During initial form build, add the term entity to the form state for use
  // during form building and processing. During a rebuild, use what is in the
  // form state.
  if (!isset($form_state['term'])) {
    $term = is_object($edit) ? $edit : (object) $edit;
    if (!isset($vocabulary) && isset($term->vid)) {
      $vocabulary = taxonomy_vocabulary_load($term->vid);
    }
    $defaults = array(
      'name' => '',
      'description' => '',
      'format' => NULL,
      'vocabulary_machine_name' => isset($vocabulary) ? $vocabulary->machine_name : NULL,
      'tid' => NULL,
      'weight' => 0,
    );
    foreach ($defaults as $key => $value) {
      if (!isset($term->$key)) {
        $term->$key = $value;
      }
    }
    $form_state['term'] = $term;
  }
  else {
    $term = $form_state['term'];
    if (!isset($vocabulary) && isset($term->vid)) {
      $vocabulary = taxonomy_vocabulary_load($term->vid);
    }
  }

  $parent = array_keys(taxonomy_get_parents($term->tid));
  $form['#term'] = (array) $term;
  $form['#term']['parent'] = $parent;
  $form['#vocabulary'] = $vocabulary;

  // Check for confirmation forms.
  if (isset($form_state['confirm_delete'])) {
    return array_merge($form, taxonomy_term_confirm_delete($form, $form_state, $term->tid));
  }

  $form['name'] = array(
    '#type' => 'textfield',
    '#title' => t('Name'),
    '#default_value' => $term->name,
    '#maxlength' => 255,
    '#required' => TRUE,
    '#weight' => -5,
  );
  $form['description'] = array(
    '#type' => 'text_format',
    '#title' => t('Description'),
    '#default_value' => $term->description,
    '#format' => $term->format,
    '#weight' => 0,
  );

  $form['vocabulary_machine_name'] = array(
    '#type' => 'value',
    '#value' => isset($term->vocabulary_machine_name) ? $term->vocabulary_machine_name : $vocabulary->name,
  );

  $langcode = entity_language('taxonomy_term', $term);
  field_attach_form('taxonomy_term', $term, $form, $form_state, $langcode);

  $form['relations'] = array(
    '#type' => 'fieldset',
    '#title' => t('Relations'),
    '#collapsible' => TRUE,
    '#collapsed' => $vocabulary->hierarchy < 2,
    '#weight' => 10,
  );

  // taxonomy_get_tree and taxonomy_get_parents may contain large numbers of
  // items so we check for taxonomy_override_selector before loading the
  // full vocabulary. Contrib modules can then intercept before
  // hook_form_alter to provide scalable alternatives.
  if (!variable_get('taxonomy_override_selector', FALSE)) {
    $parent = array_keys(taxonomy_get_parents($term->tid));
    $children = taxonomy_get_tree($vocabulary->vid, $term->tid);

    // A term can't be the child of itself, nor of its children.
    foreach ($children as $child) {
      $exclude[] = $child->tid;
    }
    $exclude[] = $term->tid;

    $tree = taxonomy_get_tree($vocabulary->vid);
    $options = array('<' . t('root') . '>');
    if (empty($parent)) {
      $parent = array(0);
    }
    foreach ($tree as $item) {
      if (!in_array($item->tid, $exclude)) {
        $options[$item->tid] = str_repeat('-', $item->depth) . $item->name;
      }
    }
    $form['relations']['parent'] = array(
      '#type' => 'select',
      '#title' => t('Parent terms'),
      '#options' => $options,
      '#default_value' => $parent,
      '#multiple' => TRUE,
    );

  }
  $form['relations']['weight'] = array(
    '#type' => 'textfield',
    '#title' => t('Weight'),
    '#size' => 6,
    '#default_value' => $term->weight,
    '#description' => t('Terms are displayed in ascending order by weight.'),
    '#required' => TRUE,
  );
  $form['vid'] = array(
    '#type' => 'value',
    '#value' => $vocabulary->vid,
  );
  $form['tid'] = array(
    '#type' => 'value',
    '#value' => $term->tid,
  );

  $form['actions'] = array('#type' => 'actions');
  $form['actions']['submit'] = array(
    '#type' => 'submit',
    '#value' => t('Save'),
    '#weight' => 5,
  );

  if ($term->tid) {
    $form['actions']['delete'] = array(
      '#type' => 'submit',
      '#value' => t('Delete'),
      '#access' => user_access("delete terms in $vocabulary->vid") || user_access('administer taxonomy'),
      '#weight' => 10,
    );
  }
  else {
    $form_state['redirect'] = $_GET['q'];
  }

  return $form;
}
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
