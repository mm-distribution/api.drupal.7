# simpletest_result_form()

- **Type:** Function
- **File:** [`modules/simpletest/simpletest.pages.inc`](_file.md), lines 206–337 · [local source](../../../../source/modules/simpletest/simpletest.pages.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.pages.inc#L206-L337)
- **Module/theme:** simpletest

## Signature

```php
function simpletest_result_form($form, &$form_state, $test_id)
```

## Documentation

```text
Test results form for $test_id.
```

## Code

```php
function simpletest_result_form($form, &$form_state, $test_id) {
  // Make sure there are test results to display and a re-run is not being performed.
  $results = array();
  if (is_numeric($test_id) && !$results = simpletest_result_get($test_id)) {
    drupal_set_message(t('No test results to display.'), 'error');
    drupal_goto('admin/config/development/testing');
    return $form;
  }

  // Load all classes and include CSS.
  drupal_add_css(drupal_get_path('module', 'simpletest') . '/simpletest.css');

  // Keep track of which test cases passed or failed.
  $filter = array(
    'pass' => array(),
    'fail' => array(),
  );

  // Summary result fieldset.
  $form['result'] = array(
    '#type' => 'fieldset',
    '#title' => t('Results'),
  );
  $form['result']['summary'] = $summary = array(
    '#theme' => 'simpletest_result_summary',
    '#pass' => 0,
    '#fail' => 0,
    '#exception' => 0,
    '#debug' => 0,
  );

  simpletest_classloader_register();

  // Cycle through each test group.
  $header = array(t('Message'), t('Group'), t('Filename'), t('Line'), t('Function'), array('colspan' => 2, 'data' => t('Status')));
  $form['result']['results'] = array();
  foreach ($results as $group => $assertions) {
    // Create group fieldset with summary information.
    $info = call_user_func(array($group, 'getInfo'));
    $form['result']['results'][$group] = array(
      '#type' => 'fieldset',
      '#title' => $info['name'],
      '#description' => $info['description'],
      '#collapsible' => TRUE,
    );
    $form['result']['results'][$group]['summary'] = $summary;
    $group_summary = &$form['result']['results'][$group]['summary'];

    // Create table of assertions for the group.
    $rows = array();
    foreach ($assertions as $assertion) {
      $row = array();
      $row[] = $assertion->message;
      $row[] = $assertion->message_group;
      $row[] = drupal_basename($assertion->file);
      $row[] = $assertion->line;
      $row[] = $assertion->function;
      $row[] = simpletest_result_status_image($assertion->status);

      $class = 'simpletest-' . $assertion->status;
      if ($assertion->message_group == 'Debug') {
        $class = 'simpletest-debug';
      }
      $rows[] = array('data' => $row, 'class' => array($class));

      $group_summary['#' . $assertion->status]++;
      $form['result']['summary']['#' . $assertion->status]++;
    }
    $form['result']['results'][$group]['table'] = array(
      '#theme' => 'table',
      '#header' => $header,
      '#rows' => $rows,
    );

    // Set summary information.
    $group_summary['#ok'] = $group_summary['#fail'] + $group_summary['#exception'] == 0;
    $form['result']['results'][$group]['#collapsed'] = $group_summary['#ok'];

    // Store test group (class) as for use in filter.
    $filter[$group_summary['#ok'] ? 'pass' : 'fail'][] = $group;
  }

  // Overal summary status.
  $form['result']['summary']['#ok'] = $form['result']['summary']['#fail'] + $form['result']['summary']['#exception'] == 0;

  // Actions.
  $form['#action'] = url('admin/config/development/testing/results/re-run');
  $form['action'] = array(
    '#type' => 'fieldset',
    '#title' => t('Actions'),
    '#attributes' => array('class' => array('container-inline')),
    '#weight' => -11,
  );

  $form['action']['filter'] = array(
    '#type' => 'select',
    '#title' => 'Filter',
    '#options' => array(
      'all' => t('All (@count)', array('@count' => count($filter['pass']) + count($filter['fail']))),
      'pass' => t('Pass (@count)', array('@count' => count($filter['pass']))),
      'fail' => t('Fail (@count)', array('@count' => count($filter['fail']))),
    ),
  );
  $form['action']['filter']['#default_value'] = ($filter['fail'] ? 'fail' : 'all');

  // Categorized test classes for to be used with selected filter value.
  $form['action']['filter_pass'] = array(
    '#type' => 'hidden',
    '#default_value' => implode(',', $filter['pass']),
  );
  $form['action']['filter_fail'] = array(
    '#type' => 'hidden',
    '#default_value' => implode(',', $filter['fail']),
  );

  $form['action']['op'] = array(
    '#type' => 'submit',
    '#value' => t('Run tests'),
  );

  $form['action']['return'] = array(
    '#type' => 'link',
    '#title' => t('Return to list'),
    '#href' => 'admin/config/development/testing',
  );

  if (is_numeric($test_id)) {
    simpletest_clean_results_table($test_id);
  }

  return $form;
}
```

---
_Drupal 7.103 · [modules/simpletest/simpletest.pages.inc](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.pages.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
