# contact_category_edit_form()

- **Type:** Function
- **File:** [`modules/contact/contact.admin.inc`](_file.md), lines 73–132 · [local source](../../../../source/modules/contact/contact.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/contact/contact.admin.inc#L73-L132)
- **Module/theme:** contact
- **Topics:** [forms](../../../topics/forms.md)

## Signature

```php
function contact_category_edit_form($form, &$form_state, array $category = array())
```

## Documentation

```text
Form constructor for the category edit form.

@param $category
  An array describing the category to be edited. May be empty for new
  categories. Recognized array keys are:
  - category: The name of the category.
  - recipients: A comma-separated list of recipients.
  - reply: (optional) The body of the auto-reply message.
  - weight: The weight of the category.
  - selected: Boolean indicating whether the category should be selected by
    default.
  - cid: The category ID for which the form is to be displayed.

@see contact_category_edit_form_validate()
@see contact_category_edit_form_submit()
@ingroup forms
```

## Code

```php
function contact_category_edit_form($form, &$form_state, array $category = array()) {
  // If this is a new category, add the default values.
  $category += array(
    'category' => '',
    'recipients' => '',
    'reply' => '',
    'weight' => 0,
    'selected' => 0,
    'cid' => NULL,
  );

  $form['category'] = array(
    '#type' => 'textfield',
    '#title' => t('Category'),
    '#maxlength' => 255,
    '#default_value' => $category['category'],
    '#description' => t("Example: 'website feedback' or 'product information'."),
    '#required' => TRUE,
  );
  $form['recipients'] = array(
    '#type' => 'textarea',
    '#title' => t('Recipients'),
    '#default_value' => $category['recipients'],
    '#description' => t("Example: 'webmaster@example.com' or 'sales@example.com,support@example.com' . To specify multiple recipients, separate each e-mail address with a comma."),
    '#required' => TRUE,
  );
  $form['reply'] = array(
    '#type' => 'textarea',
    '#title' => t('Auto-reply'),
    '#default_value' => $category['reply'],
    '#description' => t('Optional auto-reply. Leave empty if you do not want to send the user an auto-reply message.'),
  );
  $form['weight'] = array(
    '#type' => 'weight',
    '#title' => t('Weight'),
    '#default_value' => $category['weight'],
    '#description' => t('When listing categories, those with lighter (smaller) weights get listed before categories with heavier (larger) weights. Categories with equal weights are sorted alphabetically.'),
  );
  $form['selected'] = array(
    '#type' => 'select',
    '#title' => t('Selected'),
    '#options' => array(
      0 => t('No'),
      1 => t('Yes'),
    ),
    '#default_value' => $category['selected'],
    '#description' => t('Set this to <em>Yes</em> if you would like this category to be selected by default.'),
  );
  $form['cid'] = array(
    '#type' => 'value',
    '#value' => $category['cid'],
  );
  $form['actions'] = array('#type' => 'actions');
  $form['actions']['submit'] = array(
    '#type' => 'submit',
    '#value' => t('Save'),
  );

  return $form;
}
```

---
_Drupal 7.103 · [modules/contact/contact.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/contact/contact.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
