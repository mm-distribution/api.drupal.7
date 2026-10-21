# filter_admin_format_form()

- **Type:** Function
- **File:** [`modules/filter/filter.admin.inc`](_file.md), lines 154–292 · [local source](../../../../source/modules/filter/filter.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.admin.inc#L154-L292)
- **Module/theme:** filter
- **Topics:** [forms](../../../topics/forms.md)

## Signature

```php
function filter_admin_format_form($form, &$form_state, $format)
```

## Documentation

```text
Form constructor for the text format add/edit form.

@param $format
  A format object having the properties:
  - format: A machine-readable name representing the ID of the text format to
    save. If this corresponds to an existing text format, that format will be
    updated; otherwise, a new format will be created.
  - name: The title of the text format.
  - cache: An integer indicating whether the text format is cacheable (1) or
    not (0). Defaults to 1.
  - status: (optional) An integer indicating whether the text format is
    enabled (1) or not (0). Defaults to 1.
  - weight: (optional) The weight of the text format, which controls its
    placement in text format lists. If omitted, the weight is set to 0.

@see filter_admin_format_form_validate()
@see filter_admin_format_form_submit()
@ingroup forms
```

## Code

```php
function filter_admin_format_form($form, &$form_state, $format) {
  $is_fallback = ($format->format == filter_fallback_format());

  $form['#format'] = $format;
  $form['#tree'] = TRUE;
  $form['#attached']['js'][] = drupal_get_path('module', 'filter') . '/filter.admin.js';
  $form['#attached']['css'][] = drupal_get_path('module', 'filter') . '/filter.css';

  $form['name'] = array(
    '#type' => 'textfield',
    '#title' => t('Name'),
    '#default_value' => $format->name,
    '#required' => TRUE,
  );
  $form['format'] = array(
    '#type' => 'machine_name',
    '#required' => TRUE,
    '#default_value' => $format->format,
    '#maxlength' => 255,
    '#machine_name' => array(
      'exists' => 'filter_format_exists',
    ),
    '#disabled' => !empty($format->format),
  );

  // Add user role access selection.
  $form['roles'] = array(
    '#type' => 'checkboxes',
    '#title' => t('Roles'),
    '#options' => array_map('check_plain', user_roles()),
    '#disabled' => $is_fallback,
  );
  if ($is_fallback) {
    $form['roles']['#description'] = t('All roles for this text format must be enabled and cannot be changed.');
  }
  if (!empty($format->format)) {
    // If editing an existing text format, pre-select its current permissions.
    $form['roles']['#default_value'] = array_keys(filter_get_roles_by_format($format));
  }
  elseif ($admin_role = variable_get('user_admin_role', 0)) {
    // If adding a new text format and the site has an administrative role,
    // pre-select that role so as to grant administrators access to the new
    // text format permission by default.
    $form['roles']['#default_value'] = array($admin_role);
  }

  // Retrieve available filters and load all configured filters for existing
  // text formats.
  $filter_info = filter_get_filters();
  $filters = !empty($format->format) ? filter_list_format($format->format) : array();

  // Prepare filters for form sections.
  foreach ($filter_info as $name => $filter) {
    // Create an empty filter object for new/unconfigured filters.
    if (!isset($filters[$name])) {
      $filters[$name] = new stdClass();
      $filters[$name]->format = $format->format;
      $filters[$name]->module = $filter['module'];
      $filters[$name]->name = $name;
      $filters[$name]->status = 0;
      $filters[$name]->weight = $filter['weight'];
      $filters[$name]->settings = array();
    }
  }
  $form['#filters'] = $filters;

  // Filter status.
  $form['filters']['status'] = array(
    '#type' => 'item',
    '#title' => t('Enabled filters'),
    '#prefix' => '<div id="filters-status-wrapper">',
    '#suffix' => '</div>',
  );
  foreach ($filter_info as $name => $filter) {
    $form['filters']['status'][$name] = array(
      '#type' => 'checkbox',
      '#title' => $filter['title'],
      '#default_value' => $filters[$name]->status,
      '#parents' => array('filters', $name, 'status'),
      '#description' => $filter['description'],
      '#weight' => $filter['weight'],
    );
  }

  // Filter order (tabledrag).
  $form['filters']['order'] = array(
    '#type' => 'item',
    '#title' => t('Filter processing order'),
    '#theme' => 'filter_admin_format_filter_order',
  );
  foreach ($filter_info as $name => $filter) {
    $form['filters']['order'][$name]['filter'] = array(
      '#markup' => $filter['title'],
    );
    $form['filters']['order'][$name]['weight'] = array(
      '#type' => 'weight',
      '#title' => t('Weight for @title', array('@title' => $filter['title'])),
      '#title_display' => 'invisible',
      '#delta' => 50,
      '#default_value' => $filters[$name]->weight,
      '#parents' => array('filters', $name, 'weight'),
    );
    $form['filters']['order'][$name]['#weight'] = $filters[$name]->weight;
  }

  // Filter settings.
  $form['filter_settings_title'] = array(
    '#type' => 'item',
    '#title' => t('Filter settings'),
  );
  $form['filter_settings'] = array(
    '#type' => 'vertical_tabs',
  );

  foreach ($filter_info as $name => $filter) {
    if (isset($filter['settings callback']) && function_exists($filter['settings callback'])) {
      $function = $filter['settings callback'];
      // Pass along stored filter settings and default settings, but also the
      // format object and all filters to allow for complex implementations.
      $defaults = (isset($filter['default settings']) ? $filter['default settings'] : array());
      $settings_form = $function($form, $form_state, $filters[$name], $format, $defaults, $filters);
      if (!empty($settings_form)) {
        $form['filters']['settings'][$name] = array(
          '#type' => 'fieldset',
          '#title' => $filter['title'],
          '#parents' => array('filters', $name, 'settings'),
          '#weight' => $filter['weight'],
          '#group' => 'filter_settings',
        );
        $form['filters']['settings'][$name] += $settings_form;
      }
    }
  }

  $form['actions'] = array('#type' => 'actions');
  $form['actions']['submit'] = array('#type' => 'submit', '#value' => t('Save configuration'));

  return $form;
}
```

---
_Drupal 7.103 · [modules/filter/filter.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
