# system_authorized_init()

- **Type:** Function
- **File:** [`modules/system/system.module`](_file.md), lines 1807–1823 · [local source](../../../../source/modules/system/system.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module#L1807-L1823)
- **Module/theme:** system
- **Topics:** [authorize](../../../topics/authorize.md)

## Signature

```php
function system_authorized_init($callback, $file, $arguments = array(), $page_title = NULL)
```

## Documentation

```text
Setup a given callback to run via authorize.php with elevated privileges.

To use authorize.php, certain variables must be stashed into $_SESSION. This
function sets up all the necessary $_SESSION variables. The calling function
should then redirect to authorize.php, using the full path returned by
system_authorized_get_url(). That initiates the workflow that will eventually
lead to the callback being invoked. The callback will be invoked at a low
bootstrap level, without all modules being invoked, so it needs to be careful
not to assume any code exists. Example (system_authorized_run()):
@code
  system_authorized_init($callback, $file, $arguments, $page_title);
  drupal_goto(system_authorized_get_url());
@endcode
Example (update_manager_install_form_submit()):
@code
 system_authorized_init('update_authorize_run_install',
   drupal_get_path('module', 'update') . '/update.authorize.inc',
   $arguments, t('Update manager'));
 $form_state['redirect'] = system_authorized_get_url();
@endcode

@param $callback
  The name of the function to invoke once the user authorizes the operation.
@param $file
  The full path to the file where the callback function is implemented.
@param $arguments
  Optional array of arguments to pass into the callback when it is invoked.
  Note that the first argument to the callback is always the FileTransfer
  object created by authorize.php when the user authorizes the operation.
@param $page_title
  Optional string to use as the page title once redirected to authorize.php.
@return
  Nothing, this function just initializes variables in the user's session.
```

## Code

```php
function system_authorized_init($callback, $file, $arguments = array(), $page_title = NULL) {
  // First, figure out what file transfer backends the site supports, and put
  // all of those in the SESSION so that authorize.php has access to all of
  // them via the class autoloader, even without a full bootstrap.
  $_SESSION['authorize_filetransfer_info'] = drupal_get_filetransfer_info();

  // Now, define the callback to invoke.
  $_SESSION['authorize_operation'] = array(
    'callback' => $callback,
    'file' => $file,
    'arguments' => $arguments,
  );

  if (isset($page_title)) {
    $_SESSION['authorize_operation']['page_title'] = $page_title;
  }
}
```

---
_Drupal 7.103 · [modules/system/system.module](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module) · Licensed GPL-2.0-or-later (see LICENSE)._
