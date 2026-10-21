# DatabaseTasks::runTasks()

- **Type:** Method
- **File:** [`includes/install.inc`](../_file.md), lines 397–426 · [local source](../../../../source/includes/install.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/install.inc#L397-L426)
- **Class:** [DatabaseTasks](../DatabaseTasks.md)

## Signature

```php
public function runTasks()
```

## Documentation

```text
Run database tasks and tests to see if Drupal can run on the database.
```

## Code

```php
  public function runTasks() {
    // We need to establish a connection before we can run tests.
    if ($this->connect()) {
      foreach ($this->tasks as $task) {
        if (!isset($task['function'])) {
          $task['function'] = 'runTestQuery';
        }
        if (method_exists($this, $task['function'])) {
          // Returning false is fatal. No other tasks can run.
          if (FALSE === call_user_func_array(array($this, $task['function']), $task['arguments'])) {
            break;
          }
        }
        else {
          throw new DatabaseTaskException(st("Failed to run all tasks against the database server. The task %task wasn't found.", array('%task' => $task['function'])));
        }
      }
    }
    // Check for failed results and compile message
    $message = '';
    foreach ($this->results as $result => $success) {
      if (!$success) {
        $message .= '<p class="error">' . $result  . '</p>';
      }
    }
    if (!empty($message)) {
      $message = 'Resolve all issues below to continue the installation. For help configuring your database server, see the <a href="http://drupal.org/getting-started/install">installation handbook</a>, or contact your hosting provider.' . $message;
      throw new DatabaseTaskException($message);
    }
  }
```

---
_Drupal 7.103 · [includes/install.inc](https://github.com/drupal/drupal/blob/7.103/includes/install.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
