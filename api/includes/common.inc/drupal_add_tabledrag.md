# drupal_add_tabledrag()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 5165–5188 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L5165-L5188)

## Signature

```php
function drupal_add_tabledrag($table_id, $action, $relationship, $group, $subgroup = NULL, $source = NULL, $hidden = TRUE, $limit = 0)
```

## Documentation

```text
Assists in adding the tableDrag JavaScript behavior to a themed table.

Draggable tables should be used wherever an outline or list of sortable items
needs to be arranged by an end-user. Draggable tables are very flexible and
can manipulate the value of form elements placed within individual columns.

To set up a table to use drag and drop in place of weight select-lists or in
place of a form that contains parent relationships, the form must be themed
into a table. The table must have an ID attribute set. If using
theme_table(), the ID may be set as follows:
@code
$output = theme('table', array('header' => $header, 'rows' => $rows, 'attributes' => array('id' => 'my-module-table')));
return $output;
@endcode

In the theme function for the form, a special class must be added to each
form element within the same column, "grouping" them together.

In a situation where a single weight column is being sorted in the table, the
classes could be added like this (in the theme function):
@code
$form['my_elements'][$delta]['weight']['#attributes']['class'] = array('my-elements-weight');
@endcode

Each row of the table must also have a class of "draggable" in order to
enable the drag handles:
@code
$row = array(...);
$rows[] = array(
  'data' => $row,
  'class' => array('draggable'),
);
@endcode

When tree relationships are present, the two additional classes
'tabledrag-leaf' and 'tabledrag-root' can be used to refine the behavior:
- Rows with the 'tabledrag-leaf' class cannot have child rows.
- Rows with the 'tabledrag-root' class cannot be nested under a parent row.

Calling drupal_add_tabledrag() would then be written as such:
@code
drupal_add_tabledrag('my-module-table', 'order', 'sibling', 'my-elements-weight');
@endcode

In a more complex case where there are several groups in one column (such as
the block regions on the admin/structure/block page), a separate subgroup
class must also be added to differentiate the groups.
@code
$form['my_elements'][$region][$delta]['weight']['#attributes']['class'] = array('my-elements-weight', 'my-elements-weight-' . $region);
@endcode

$group is still 'my-element-weight', and the additional $subgroup variable
will be passed in as 'my-elements-weight-' . $region. This also means that
you'll need to call drupal_add_tabledrag() once for every region added.

@code
foreach ($regions as $region) {
  drupal_add_tabledrag('my-module-table', 'order', 'sibling', 'my-elements-weight', 'my-elements-weight-' . $region);
}
@endcode

In a situation where tree relationships are present, adding multiple
subgroups is not necessary, because the table will contain indentations that
provide enough information about the sibling and parent relationships. See
theme_menu_overview_form() for an example creating a table containing parent
relationships.

Note that this function should be called from the theme layer, such as in a
.tpl.php file, theme_ function, or in a template_preprocess function, not in
a form declaration. Though the same JavaScript could be added to the page
using drupal_add_js() directly, this function helps keep template files
clean and readable. It also prevents tabledrag.js from being added twice
accidentally.

@param $table_id
  String containing the target table's id attribute. If the table does not
  have an id, one will need to be set, such as <table id="my-module-table">.
@param $action
  String describing the action to be done on the form item. Either 'match'
  'depth', or 'order'. Match is typically used for parent relationships.
  Order is typically used to set weights on other form elements with the same
  group. Depth updates the target element with the current indentation.
@param $relationship
  String describing where the $action variable should be performed. Either
  'parent', 'sibling', 'group', or 'self'. Parent will only look for fields
  up the tree. Sibling will look for fields in the same group in rows above
  and below it. Self affects the dragged row itself. Group affects the
  dragged row, plus any children below it (the entire dragged group).
@param $group
  A class name applied on all related form elements for this action.
@param $subgroup
  (optional) If the group has several subgroups within it, this string should
  contain the class name identifying fields in the same subgroup.
@param $source
  (optional) If the $action is 'match', this string should contain the class
  name identifying what field will be used as the source value when matching
  the value in $subgroup.
@param $hidden
  (optional) The column containing the field elements may be entirely hidden
  from view dynamically when the JavaScript is loaded. Set to FALSE if the
  column should not be hidden.
@param $limit
  (optional) Limit the maximum amount of parenting in this table.
@see block-admin-display-form.tpl.php
@see theme_menu_overview_form()
```

## Code

```php
function drupal_add_tabledrag($table_id, $action, $relationship, $group, $subgroup = NULL, $source = NULL, $hidden = TRUE, $limit = 0) {
  $js_added = &drupal_static(__FUNCTION__, FALSE);
  if (!$js_added) {
    // Add the table drag JavaScript to the page before the module JavaScript
    // to ensure that table drag behaviors are registered before any module
    // uses it.
    drupal_add_library('system', 'jquery.cookie');
    drupal_add_js('misc/tabledrag.js', array('weight' => -1));
    $js_added = TRUE;
  }

  // If a subgroup or source isn't set, assume it is the same as the group.
  $target = isset($subgroup) ? $subgroup : $group;
  $source = isset($source) ? $source : $target;
  $settings['tableDrag'][$table_id][$group][] = array(
    'target' => $target,
    'source' => $source,
    'relationship' => $relationship,
    'action' => $action,
    'hidden' => $hidden,
    'limit' => $limit,
  );
  drupal_add_js($settings, 'setting');
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
