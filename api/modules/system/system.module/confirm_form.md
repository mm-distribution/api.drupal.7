# confirm_form()

- **Type:** Function
- **File:** [`modules/system/system.module`](_file.md), lines 2916–2952 · [local source](../../../../source/modules/system/system.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module#L2916-L2952)
- **Module/theme:** system

## Signature

```php
function confirm_form($form, $question, $path, $description = NULL, $yes = NULL, $no = NULL, $name = 'confirm')
```

## Documentation

```text
Generates a form array for a confirmation form.

This function returns a complete form array for confirming an action. The
form contains a confirm button as well as a cancellation link that allows a
user to abort the action.

If the submit handler for a form that implements confirm_form() is invoked,
the user successfully confirmed the action. You should never directly
inspect $_POST to see if an action was confirmed.

Note - if the parameters $question, $description, $yes, or $no could contain
any user input (such as node titles or taxonomy terms), it is the
responsibility of the code calling confirm_form() to sanitize them first with
a function like check_plain() or filter_xss().

@param $form
  Additional elements to add to the form. These can be regular form elements,
  #value elements, etc., and their values will be available to the submit
  handler.
@param $question
  The question to ask the user (e.g. "Are you sure you want to delete the
  block <em>foo</em>?"). The page title will be set to this value.
@param $path
  The page to go to if the user cancels the action. This can be either:
  - A string containing a Drupal path.
  - An associative array with a 'path' key. Additional array values are
    passed as the $options parameter to l().
  If the 'destination' query parameter is set in the URL when viewing a
  confirmation form, that value will be used instead of $path.
@param $description
  Additional text to display. Defaults to t('This action cannot be undone.').
@param $yes
  A caption for the button that confirms the action (e.g. "Delete",
  "Replace", ...). Defaults to t('Confirm').
@param $no
  A caption for the link which cancels the action (e.g. "Cancel"). Defaults
  to t('Cancel').
@param $name
  The internal name used to refer to the confirmation item.

@return
  The form array.
```

## Code

```php
function confirm_form($form, $question, $path, $description = NULL, $yes = NULL, $no = NULL, $name = 'confirm') {
  $description = isset($description) ? $description : t('This action cannot be undone.');

  // Prepare cancel link.
  if (isset($_GET['destination'])) {
    $options = drupal_parse_url($_GET['destination']);
  }
  elseif (is_array($path)) {
    $options = $path;
  }
  else {
    $options = array('path' => $path);
  }

  drupal_set_title($question, PASS_THROUGH);

  $form['#attributes']['class'][] = 'confirmation';
  $form['description'] = array('#markup' => $description);
  $form[$name] = array('#type' => 'hidden', '#value' => 1);

  $form['actions'] = array('#type' => 'actions');
  $form['actions']['submit'] = array(
    '#type' => 'submit',
    '#value' => $yes ? $yes : t('Confirm'),
  );
  $form['actions']['cancel'] = array(
    '#type' => 'link',
    '#title' => $no ? $no : t('Cancel'),
    '#href' => $options['path'],
    '#options' => $options,
  );
  // By default, render the form using theme_confirm_form().
  if (!isset($form['#theme'])) {
    $form['#theme'] = 'confirm_form';
  }
  return $form;
}
```

---
_Drupal 7.103 · [modules/system/system.module](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module) · Licensed GPL-2.0-or-later (see LICENSE)._
