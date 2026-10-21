# hook_form()

- **Type:** Hook (documentation function)
- **File:** [`modules/node/node.api.php`](_file.md), lines 1123–1152 · [local source](../../../../source/modules/node/node.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.api.php#L1123-L1152)
- **Module/theme:** node
- **Topics:** [hooks](../../../topics/hooks.md), [node_api_hooks](../../../topics/node_api_hooks.md)

## Signature

```php
function hook_form($node, &$form_state)
```

## Documentation

```text
Display a node editing form.

This is a node-type-specific hook, which is invoked only for the node type
being affected. See
@link node_api_hooks Node API hooks @endlink for more information.

Use hook_form_BASE_FORM_ID_alter(), with base form ID 'node_form', to alter
node forms for all node types.

This hook, implemented by node modules, is called to retrieve the form
that is displayed to create or edit a node. This form is displayed at path
node/add/[node type] or node/[node ID]/edit.

The submit and preview buttons, administrative and display controls, and
sections added by other modules (such as path settings, menu settings,
comment settings, and fields managed by the Field UI module) are
displayed automatically by the node module. This hook just needs to
return the node title and form editing fields specific to the node type.

@param $node
  The node being added or edited.
@param $form_state
  The form state array.

@return
  An array containing the title and any custom form elements to be displayed
  in the node editing form.

@ingroup node_api_hooks
```

## Code

```php
function hook_form($node, &$form_state) {
  $type = node_type_get_type($node);

  $form['title'] = array(
    '#type' => 'textfield',
    '#title' => check_plain($type->title_label),
    '#default_value' => !empty($node->title) ? $node->title : '',
    '#required' => TRUE, '#weight' => -5
  );

  $form['field1'] = array(
    '#type' => 'textfield',
    '#title' => t('Custom field'),
    '#default_value' => $node->field1,
    '#maxlength' => 127,
  );
  $form['selectbox'] = array(
    '#type' => 'select',
    '#title' => t('Select box'),
    '#default_value' => $node->selectbox,
    '#options' => array(
      1 => 'Option A',
      2 => 'Option B',
      3 => 'Option C',
    ),
    '#description' => t('Choose an option.'),
  );

  return $form;
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_form()".

- [blog_form()](../../blog/blog.module/blog_form.md) — `modules/blog/blog.module`
- [forum_form()](../../forum/forum.module/forum_form.md) — `modules/forum/forum.module`
- [node_content_form()](../node.module/node_content_form.md) — `modules/node/node.module`
- [poll_form()](../../poll/poll.module/poll_form.md) — `modules/poll/poll.module`

---
_Drupal 7.103 · [modules/node/node.api.php](https://github.com/drupal/drupal/blob/7.103/modules/node/node.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
