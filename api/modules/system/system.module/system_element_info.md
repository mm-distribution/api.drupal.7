# system_element_info()

- **Type:** Function
- **File:** [`modules/system/system.module`](_file.md), lines 298–530 · [local source](../../../../source/modules/system/system.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module#L298-L530)
- **Module/theme:** system
- **Implements:** [hook_element_info()](../system.api.php/hook_element_info.md)

## Signature

```php
function system_element_info()
```

## Documentation

```text
Implements hook_element_info().
```

## Code

```php
function system_element_info() {
  // Top level elements.
  $types['form'] = array(
    '#method' => 'post',
    '#action' => request_uri(),
    '#theme_wrappers' => array('form'),
  );
  $types['page'] = array(
    '#show_messages' => TRUE,
    '#theme' => 'page',
    '#theme_wrappers' => array('html'),
  );
  // By default, we don't want Ajax commands being rendered in the context of an
  // HTML page, so we don't provide defaults for #theme or #theme_wrappers.
  // However, modules can set these properties (for example, to provide an HTML
  // debugging page that displays rather than executes Ajax commands).
  $types['ajax'] = array(
    '#header' => TRUE,
    '#commands' => array(),
    '#error' => NULL,
  );
  $types['html_tag'] = array(
    '#theme' => 'html_tag',
    '#pre_render' => array('drupal_pre_render_conditional_comments'),
    '#attributes' => array(),
    '#value' => NULL,
  );
  $types['styles'] = array(
    '#items' => array(),
    '#pre_render' => array('drupal_pre_render_styles'),
    '#group_callback' => 'drupal_group_css',
    '#aggregate_callback' => 'drupal_aggregate_css',
  );
  $types['scripts'] = array(
    '#items' => array(),
    '#pre_render' => array('drupal_pre_render_scripts'),
  );

  // Input elements.
  $types['submit'] = array(
    '#input' => TRUE,
    '#name' => 'op',
    '#button_type' => 'submit',
    '#executes_submit_callback' => TRUE,
    '#limit_validation_errors' => FALSE,
    '#process' => array('ajax_process_form', 'form_process_button'),
    '#theme_wrappers' => array('button'),
  );
  $types['button'] = array(
    '#input' => TRUE,
    '#name' => 'op',
    '#button_type' => 'submit',
    '#executes_submit_callback' => FALSE,
    '#limit_validation_errors' => FALSE,
    '#process' => array('ajax_process_form', 'form_process_button'),
    '#theme_wrappers' => array('button'),
  );
  $types['image_button'] = array(
    '#input' => TRUE,
    '#button_type' => 'submit',
    '#executes_submit_callback' => TRUE,
    '#limit_validation_errors' => FALSE,
    '#process' => array('ajax_process_form', 'form_process_button'),
    '#return_value' => TRUE,
    '#has_garbage_value' => TRUE,
    '#src' => NULL,
    '#theme_wrappers' => array('image_button'),
  );
  $types['textfield'] = array(
    '#input' => TRUE,
    '#size' => 60,
    '#maxlength' => 128,
    '#autocomplete_path' => FALSE,
    '#process' => array('form_process_autocomplete', 'ajax_process_form'),
    '#theme' => 'textfield',
    '#theme_wrappers' => array('form_element'),
  );
  $types['machine_name'] = array(
    '#input' => TRUE,
    '#default_value' => NULL,
    '#required' => TRUE,
    '#maxlength' => 64,
    '#size' => 60,
    '#autocomplete_path' => FALSE,
    '#process' => array('form_process_machine_name', 'ajax_process_form'),
    '#element_validate' => array('form_validate_machine_name'),
    '#theme' => 'textfield',
    '#theme_wrappers' => array('form_element'),
    // Use the same value callback as for textfields; this ensures that we only
    // get string values.
    '#value_callback' => 'form_type_textfield_value',
  );
  $types['password'] = array(
    '#input' => TRUE,
    '#size' => 60,
    '#maxlength' => 128,
    '#process' => array('ajax_process_form'),
    '#theme' => 'password',
    '#theme_wrappers' => array('form_element'),
    // Use the same value callback as for textfields; this ensures that we only
    // get string values.
    '#value_callback' => 'form_type_textfield_value',
  );
  $types['password_confirm'] = array(
    '#input' => TRUE,
    '#process' => array('form_process_password_confirm', 'user_form_process_password_confirm'),
    '#theme_wrappers' => array('form_element'),
  );
  $types['textarea'] = array(
    '#input' => TRUE,
    '#cols' => 60,
    '#rows' => 5,
    '#resizable' => TRUE,
    '#process' => array('ajax_process_form'),
    '#theme' => 'textarea',
    '#theme_wrappers' => array('form_element'),
  );
  $types['radios'] = array(
    '#input' => TRUE,
    '#process' => array('form_process_radios'),
    '#theme_wrappers' => array('radios'),
    '#pre_render' => array('form_pre_render_conditional_form_element'),
  );
  $types['radio'] = array(
    '#input' => TRUE,
    '#default_value' => NULL,
    '#process' => array('ajax_process_form'),
    '#theme' => 'radio',
    '#theme_wrappers' => array('form_element'),
    '#title_display' => 'after',
  );
  $types['checkboxes'] = array(
    '#input' => TRUE,
    '#process' => array('form_process_checkboxes'),
    '#theme_wrappers' => array('checkboxes'),
    '#pre_render' => array('form_pre_render_conditional_form_element'),
  );
  $types['checkbox'] = array(
    '#input' => TRUE,
    '#return_value' => 1,
    '#theme' => 'checkbox',
    '#process' => array('form_process_checkbox', 'ajax_process_form'),
    '#theme_wrappers' => array('form_element'),
    '#title_display' => 'after',
  );
  $types['select'] = array(
    '#input' => TRUE,
    '#multiple' => FALSE,
    '#process' => array('form_process_select', 'ajax_process_form'),
    '#theme' => 'select',
    '#theme_wrappers' => array('form_element'),
  );
  $types['weight'] = array(
    '#input' => TRUE,
    '#delta' => 10,
    '#default_value' => 0,
    '#process' => array('form_process_weight', 'ajax_process_form'),
  );
  $types['date'] = array(
    '#input' => TRUE,
    '#element_validate' => array('date_validate'),
    '#process' => array('form_process_date'),
    '#theme' => 'date',
    '#theme_wrappers' => array('form_element'),
  );
  $types['file'] = array(
    '#input' => TRUE,
    '#size' => 60,
    '#theme' => 'file',
    '#theme_wrappers' => array('form_element'),
  );
  $types['tableselect'] = array(
    '#input' => TRUE,
    '#js_select' => TRUE,
    '#multiple' => TRUE,
    '#process' => array('form_process_tableselect'),
    '#options' => array(),
    '#empty' => '',
    '#theme' => 'tableselect',
  );

  // Form structure.
  $types['item'] = array(
    '#markup' => '',
    '#pre_render' => array('drupal_pre_render_markup'),
    '#theme_wrappers' => array('form_element'),
  );
  $types['hidden'] = array(
    '#input' => TRUE,
    '#process' => array('ajax_process_form'),
    '#theme' => 'hidden',
  );
  $types['value'] = array(
    '#input' => TRUE,
  );
  $types['markup'] = array(
    '#markup' => '',
    '#pre_render' => array('drupal_pre_render_markup'),
  );
  $types['link'] = array(
    '#pre_render' => array('drupal_pre_render_link', 'drupal_pre_render_markup'),
  );
  $types['fieldset'] = array(
    '#collapsible' => FALSE,
    '#collapsed' => FALSE,
    '#value' => NULL,
    '#process' => array('form_process_fieldset', 'ajax_process_form'),
    '#pre_render' => array('form_pre_render_fieldset'),
    '#theme_wrappers' => array('fieldset'),
  );
  $types['vertical_tabs'] = array(
    '#theme_wrappers' => array('vertical_tabs'),
    '#default_tab' => '',
    '#process' => array('form_process_vertical_tabs'),
  );

  $types['container'] = array(
    '#theme_wrappers' => array('container'),
    '#process' => array('form_process_container'),
  );
  $types['actions'] = array(
    '#theme_wrappers' => array('container'),
    '#process' => array('form_process_actions', 'form_process_container'),
    '#weight' => 100,
  );

  $types['token'] = array(
    '#input' => TRUE,
    '#theme' => 'hidden',
  );

  return $types;
}
```

---
_Drupal 7.103 · [modules/system/system.module](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module) · Licensed GPL-2.0-or-later (see LICENSE)._
