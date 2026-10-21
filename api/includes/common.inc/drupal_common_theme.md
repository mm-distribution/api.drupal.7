# drupal_common_theme()

- **Type:** Function
- **File:** [`includes/common.inc`](_file.md), lines 7074–7284 · [local source](../../../source/includes/common.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/common.inc#L7074-L7284)

## Signature

```php
function drupal_common_theme()
```

## Documentation

```text
Provides theme registration for themes across .inc files.
```

## Code

```php
function drupal_common_theme() {
  return array(
    // From theme.inc.
    'html' => array(
      'render element' => 'page',
      'template' => 'html',
    ),
    'page' => array(
      'render element' => 'page',
      'template' => 'page',
    ),
    'region' => array(
      'render element' => 'elements',
      'template' => 'region',
    ),
    'status_messages' => array(
      'variables' => array('display' => NULL),
    ),
    'link' => array(
      'variables' => array('text' => NULL, 'path' => NULL, 'options' => array()),
    ),
    'links' => array(
      'variables' => array('links' => NULL, 'attributes' => array('class' => array('links')), 'heading' => array()),
    ),
    'image' => array(
      // HTML 4 and XHTML 1.0 always require an alt attribute. The HTML 5 draft
      // allows the alt attribute to be omitted in some cases. Therefore,
      // default the alt attribute to an empty string, but allow code calling
      // theme('image') to pass explicit NULL for it to be omitted. Usually,
      // neither omission nor an empty string satisfies accessibility
      // requirements, so it is strongly encouraged for code calling
      // theme('image') to pass a meaningful value for the alt variable.
      // - http://www.w3.org/TR/REC-html40/struct/objects.html#h-13.8
      // - http://www.w3.org/TR/xhtml1/dtds.html
      // - http://dev.w3.org/html5/spec/Overview.html#alt
      // The title attribute is optional in all cases, so it is omitted by
      // default.
      'variables' => array('path' => NULL, 'width' => NULL, 'height' => NULL, 'alt' => '', 'title' => NULL, 'attributes' => array()),
    ),
    'breadcrumb' => array(
      'variables' => array('breadcrumb' => NULL),
    ),
    'help' => array(
      'variables' => array(),
    ),
    'table' => array(
      'variables' => array(
        'header' => NULL,
        'footer' => NULL,
        'rows' => NULL,
        'attributes' => array(),
        'caption' => NULL,
        'colgroups' => array(),
        'sticky' => TRUE,
        'empty' => '',
      ),
    ),
    'tablesort_indicator' => array(
      'variables' => array('style' => NULL),
    ),
    'mark' => array(
      'variables' => array('type' => MARK_NEW),
    ),
    'item_list' => array(
      'variables' => array('items' => array(), 'title' => NULL, 'type' => 'ul', 'attributes' => array()),
    ),
    'more_help_link' => array(
      'variables' => array('url' => NULL),
    ),
    'feed_icon' => array(
      'variables' => array('url' => NULL, 'title' => NULL),
    ),
    'more_link' => array(
      'variables' => array('url' => NULL, 'title' => NULL)
    ),
    'username' => array(
      'variables' => array('account' => NULL),
    ),
    'progress_bar' => array(
      'variables' => array('percent' => NULL, 'message' => NULL),
    ),
    'indentation' => array(
      'variables' => array('size' => 1),
    ),
    'html_tag' => array(
      'render element' => 'element',
    ),
    // From theme.maintenance.inc.
    'maintenance_page' => array(
      'variables' => array('content' => NULL, 'show_messages' => TRUE),
      'template' => 'maintenance-page',
    ),
    'update_page' => array(
      'variables' => array('content' => NULL, 'show_messages' => TRUE),
    ),
    'install_page' => array(
      'variables' => array('content' => NULL),
    ),
    'task_list' => array(
      'variables' => array('items' => NULL, 'active' => NULL),
    ),
    'authorize_message' => array(
      'variables' => array('message' => NULL, 'success' => TRUE),
    ),
    'authorize_report' => array(
      'variables' => array('messages' => array()),
    ),
    // From pager.inc.
    'pager' => array(
      'variables' => array('tags' => array(), 'element' => 0, 'parameters' => array(), 'quantity' => 9),
    ),
    'pager_first' => array(
      'variables' => array('text' => NULL, 'element' => 0, 'parameters' => array()),
    ),
    'pager_previous' => array(
      'variables' => array('text' => NULL, 'element' => 0, 'interval' => 1, 'parameters' => array()),
    ),
    'pager_next' => array(
      'variables' => array('text' => NULL, 'element' => 0, 'interval' => 1, 'parameters' => array()),
    ),
    'pager_last' => array(
      'variables' => array('text' => NULL, 'element' => 0, 'parameters' => array()),
    ),
    'pager_link' => array(
      'variables' => array('text' => NULL, 'page_new' => NULL, 'element' => NULL, 'parameters' => array(), 'attributes' => array()),
    ),
    // From menu.inc.
    'menu_link' => array(
      'render element' => 'element',
    ),
    'menu_tree' => array(
      'render element' => 'tree',
    ),
    'menu_local_task' => array(
      'render element' => 'element',
    ),
    'menu_local_action' => array(
      'render element' => 'element',
    ),
    'menu_local_tasks' => array(
      'variables' => array('primary' => array(), 'secondary' => array()),
    ),
    // From form.inc.
    'select' => array(
      'render element' => 'element',
    ),
    'fieldset' => array(
      'render element' => 'element',
    ),
    'radio' => array(
      'render element' => 'element',
    ),
    'radios' => array(
      'render element' => 'element',
    ),
    'date' => array(
      'render element' => 'element',
    ),
    'exposed_filters' => array(
      'render element' => 'form',
    ),
    'checkbox' => array(
      'render element' => 'element',
    ),
    'checkboxes' => array(
      'render element' => 'element',
    ),
    'button' => array(
      'render element' => 'element',
    ),
    'image_button' => array(
      'render element' => 'element',
    ),
    'hidden' => array(
      'render element' => 'element',
    ),
    'textfield' => array(
      'render element' => 'element',
    ),
    'form' => array(
      'render element' => 'element',
    ),
    'textarea' => array(
      'render element' => 'element',
    ),
    'password' => array(
      'render element' => 'element',
    ),
    'file' => array(
      'render element' => 'element',
    ),
    'tableselect' => array(
      'render element' => 'element',
    ),
    'form_element' => array(
      'render element' => 'element',
    ),
    'form_required_marker' => array(
      'render element' => 'element',
    ),
    'form_element_label' => array(
      'render element' => 'element',
    ),
    'vertical_tabs' => array(
      'render element' => 'element',
    ),
    'container' => array(
      'render element' => 'element',
    ),
  );
}
```

---
_Drupal 7.103 · [includes/common.inc](https://github.com/drupal/drupal/blob/7.103/includes/common.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
