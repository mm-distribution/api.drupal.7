# database_test_theme_tablesort()

- **Type:** Function
- **File:** [`modules/simpletest/tests/database_test.module`](_file.md), lines 201–241 · [local source](../../../../../source/modules/simpletest/tests/database_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.module#L201-L241)
- **Module/theme:** batch_test

## Signature

```php
function database_test_theme_tablesort($form, &$form_state)
```

## Documentation

```text
Output a form without setting a header sort.
```

## Code

```php
function database_test_theme_tablesort($form, &$form_state) {
  $header = array(
    'username' => array('data' => t('Username'), 'field' => 'u.name'),
    'status' => array('data' => t('Status'), 'field' => 'u.status'),
  );

  $query = db_select('users', 'u');
  $query->condition('u.uid', 0, '<>');
  user_build_filter_query($query);

  $count_query = clone $query;
  $count_query->addExpression('COUNT(u.uid)');

  $query = $query->extend('PagerDefault')->extend('TableSort');
  $query
    ->fields('u', array('uid', 'name', 'status', 'created', 'access'))
    ->limit(50)
    ->orderByHeader($header)
    ->setCountQuery($count_query);
  $result = $query->execute();

  $options = array();

  $status = array(t('blocked'), t('active'));
  $accounts = array();
  foreach ($result as $account) {
    $options[$account->uid] = array(
      'username' => check_plain($account->name),
      'status' =>  $status[$account->status],
    );
  }

  $form['accounts'] = array(
    '#type' => 'tableselect',
    '#header' => $header,
    '#options' => $options,
    '#empty' => t('No people available.'),
  );

  return $form;
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/database_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/database_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
