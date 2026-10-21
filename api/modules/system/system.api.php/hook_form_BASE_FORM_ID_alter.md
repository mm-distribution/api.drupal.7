# hook_form_BASE_FORM_ID_alter()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 1757–1768 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L1757-L1768)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_form_BASE_FORM_ID_alter(&$form, &$form_state, $form_id)
```

## Documentation

```text
Provide a form-specific alteration for shared ('base') forms.

By default, when drupal_get_form() is called, Drupal looks for a function
with the same name as the form ID, and uses that function to build the form.
In contrast, base forms allow multiple form IDs to be mapped to a single base
(also called 'factory') form function.

Modules can implement hook_form_BASE_FORM_ID_alter() to modify a specific
base form, rather than implementing hook_form_alter() and checking for
conditions that would identify the shared form constructor.

To identify the base form ID for a particular form (or to determine whether
one exists) check the $form_state. The base form ID is stored under
$form_state['build_info']['base_form_id'].

See hook_forms() for more information on how to implement base forms in
Drupal.

Form alter hooks are called in the following order: hook_form_alter(),
hook_form_BASE_FORM_ID_alter(), hook_form_FORM_ID_alter(). See
hook_form_alter() for more details.

@param $form
  Nested array of form elements that comprise the form.
@param $form_state
  A keyed array containing the current state of the form.
@param $form_id
  String representing the name of the form itself. Typically this is the
  name of the function that generated the form.

@see hook_form_alter()
@see hook_form_FORM_ID_alter()
@see drupal_prepare_form()
@see hook_forms()
```

## Code

```php
function hook_form_BASE_FORM_ID_alter(&$form, &$form_state, $form_id) {
  // Modification for the form with the given BASE_FORM_ID goes here. For
  // example, if BASE_FORM_ID is "node_form", this code would run on every
  // node form, regardless of node type.

  // Add a checkbox to the node form about agreeing to terms of use.
  $form['terms_of_use'] = array(
    '#type' => 'checkbox',
    '#title' => t("I agree with the website's terms and conditions."),
    '#required' => TRUE,
  );
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_form_BASE_FORM_ID_alter()".

- [book_form_node_form_alter()](../../book/book.module/book_form_node_form_alter.md) — `modules/book/book.module`
- [comment_form_node_form_alter()](../../comment/comment.module/comment_form_node_form_alter.md) — `modules/comment/comment.module`
- [forum_form_node_form_alter()](../../forum/forum.module/forum_form_node_form_alter.md) — `modules/forum/forum.module`
- [locale_form_node_form_alter()](../../locale/locale.module/locale_form_node_form_alter.md) — `modules/locale/locale.module`
- [menu_form_node_form_alter()](../../menu/menu.module/menu_form_node_form_alter.md) — `modules/menu/menu.module`
- [node_access_test_form_node_form_alter()](../../node/tests/node_access_test.module/node_access_test_form_node_form_alter.md) — `modules/node/tests/node_access_test.module`
- [path_form_node_form_alter()](../../path/path.module/path_form_node_form_alter.md) — `modules/path/path.module`
- [translation_form_node_form_alter()](../../translation/translation.module/translation_form_node_form_alter.md) — `modules/translation/translation.module`

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
