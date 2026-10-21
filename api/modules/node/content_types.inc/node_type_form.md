# node_type_form()

- **Type:** Function
- **File:** [`modules/node/content_types.inc`](_file.md), lines 88–242 · [local source](../../../../source/modules/node/content_types.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/content_types.inc#L88-L242)
- **Module/theme:** node
- **Topics:** [forms](../../../topics/forms.md)

## Signature

```php
function node_type_form($form, &$form_state, $type = NULL)
```

## Documentation

```text
Form constructor for the node type editing form.

@param $type
  (optional) An object representing the node type, when editing an existing
  node type.

@see node_type_form_validate()
@see node_type_form_submit()
@ingroup forms
```

## Code

```php
function node_type_form($form, &$form_state, $type = NULL) {
  if (!isset($type->type)) {
    // This is a new type. Node module managed types are custom and unlocked.
    $type = node_type_set_defaults(array('custom' => 1, 'locked' => 0));
  }

  // Make the type object available to implementations of hook_form_alter.
  $form['#node_type'] = $type;

  $form['name'] = array(
    '#title' => t('Name'),
    '#type' => 'textfield',
    '#default_value' => $type->name,
    '#description' => t('The human-readable name of this content type. This text will be displayed as part of the list on the <em>Add new content</em> page. It is recommended that this name begin with a capital letter and contain only letters, numbers, and spaces. This name must be unique.'),
    '#required' => TRUE,
    '#size' => 30,
  );

  $form['type'] = array(
    '#type' => 'machine_name',
    '#default_value' => $type->type,
    '#maxlength' => 32,
    '#disabled' => $type->locked,
    '#machine_name' => array(
      'exists' => 'node_type_load',
    ),
    '#description' => t('A unique machine-readable name for this content type. It must only contain lowercase letters, numbers, and underscores. This name will be used for constructing the URL of the %node-add page, in which underscores will be converted into hyphens.', array(
      '%node-add' => t('Add new content'),
    )),
  );

  $form['description'] = array(
    '#title' => t('Description'),
    '#type' => 'textarea',
    '#default_value' => $type->description,
    '#description' => t('Describe this content type. The text will be displayed on the <em>Add new content</em> page.'),
  );

  $form['additional_settings'] = array(
    '#type' => 'vertical_tabs',
    '#attached' => array(
      'js' => array(drupal_get_path('module', 'node') . '/content_types.js'),
    ),
  );

  $form['submission'] = array(
    '#type' => 'fieldset',
    '#title' => t('Submission form settings'),
    '#collapsible' => TRUE,
    '#group' => 'additional_settings',
  );
  $form['submission']['title_label'] = array(
    '#title' => t('Title field label'),
    '#type' => 'textfield',
    '#default_value' => $type->title_label,
    '#required' => TRUE,
  );
  if (!$type->has_title) {
    // Avoid overwriting a content type that intentionally does not have a
    // title field.
    $form['submission']['title_label']['#attributes'] = array('disabled' => 'disabled');
    $form['submission']['title_label']['#description'] = t('This content type does not have a title field.');
    $form['submission']['title_label']['#required'] = FALSE;
  }
  $form['submission']['node_preview'] = array(
    '#type' => 'radios',
    '#title' => t('Preview before submitting'),
    '#default_value' => variable_get('node_preview_' . $type->type, DRUPAL_OPTIONAL),
    '#options' => array(
      DRUPAL_DISABLED => t('Disabled'),
      DRUPAL_OPTIONAL => t('Optional'),
      DRUPAL_REQUIRED => t('Required'),
    ),
  );
  $form['submission']['help']  = array(
    '#type' => 'textarea',
    '#title' => t('Explanation or submission guidelines'),
    '#default_value' => $type->help,
    '#description' => t('This text will be displayed at the top of the page when creating or editing content of this type.'),
  );
  $form['workflow'] = array(
    '#type' => 'fieldset',
    '#title' => t('Publishing options'),
    '#collapsible' => TRUE,
    '#collapsed' => TRUE,
    '#group' => 'additional_settings',
  );
  $form['workflow']['node_options'] = array('#type' => 'checkboxes',
    '#title' => t('Default options'),
    '#default_value' => variable_get('node_options_' . $type->type, array('status', 'promote')),
    '#options' => array(
      'status' => t('Published'),
      'promote' => t('Promoted to front page'),
      'sticky' => t('Sticky at top of lists'),
      'revision' => t('Create new revision'),
    ),
    '#description' => t('Users with the <em>Administer content</em> permission will be able to override these options.'),
  );
  $form['display'] = array(
    '#type' => 'fieldset',
    '#title' => t('Display settings'),
    '#collapsible' => TRUE,
    '#collapsed' => TRUE,
    '#group' => 'additional_settings',
  );
  $form['display']['node_submitted'] = array(
    '#type' => 'checkbox',
    '#title' => t('Display author and date information.'),
    '#default_value' => variable_get('node_submitted_' . $type->type, TRUE),
    '#description' => t('Author username and publish date will be displayed.'),
  );
  $form['old_type'] = array(
    '#type' => 'value',
    '#value' => $type->type,
  );
  $form['orig_type'] = array(
    '#type' => 'value',
    '#value' => isset($type->orig_type) ? $type->orig_type : '',
  );
  $form['base'] = array(
    '#type' => 'value',
    '#value' => $type->base,
  );
  $form['custom'] = array(
    '#type' => 'value',
    '#value' => $type->custom,
  );
  $form['modified'] = array(
    '#type' => 'value',
    '#value' => $type->modified,
  );
  $form['locked'] = array(
    '#type' => 'value',
    '#value' => $type->locked,
  );

  $form['actions'] = array('#type' => 'actions');
  $form['actions']['submit'] = array(
    '#type' => 'submit',
    '#value' => t('Save content type'),
    '#weight' => 40,
  );

  if ($type->custom) {
    if (!empty($type->type)) {
      $form['actions']['delete'] = array(
        '#type' => 'submit',
        '#value' => t('Delete content type'),
        '#weight' => 45,
      );
    }
  }

  return $form;
}
```

---
_Drupal 7.103 · [modules/node/content_types.inc](https://github.com/drupal/drupal/blob/7.103/modules/node/content_types.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
