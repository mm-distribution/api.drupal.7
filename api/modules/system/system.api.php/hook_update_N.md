# hook_update_N()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 3499–3544 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L3499-L3544)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_update_N(&$sandbox)
```

## Documentation

```text
Perform a single update.

For each change that requires one or more actions to be performed when
updating a site, add a new hook_update_N(), which will be called by
update.php. The documentation block preceding this function is stripped of
newlines and used as the description for the update on the pending updates
task list. Schema updates should adhere to the
@link http://drupal.org/node/150215 Schema API. @endlink

Implementations of hook_update_N() are named (module name)_update_(number).
The numbers are composed of three parts:
- 1 digit for Drupal core compatibility.
- 1 digit for your module's major release version (e.g., is this the 7.x-1.*
  (1) or 7.x-2.* (2) series of your module?). This digit should be 0 for
  initial porting of your module to a new Drupal core API.
- 2 digits for sequential counting, starting with 00.

Examples:
- mymodule_update_7000(): This is the required update for mymodule to run
  with Drupal core API 7.x when upgrading from Drupal core API 6.x.
- mymodule_update_7100(): This is the first update to get the database ready
  to run mymodule 7.x-1.*.
- mymodule_update_7200(): This is the first update to get the database ready
  to run mymodule 7.x-2.*. Users can directly update from 6.x-2.* to 7.x-2.*
  and they get all 70xx and 72xx updates, but not 71xx updates, because
  those reside in the 7.x-1.x branch only.

A good rule of thumb is to remove updates older than two major releases of
Drupal. See hook_update_last_removed() to notify Drupal about the removals.
For further information about releases and release numbers see:
@link http://drupal.org/node/711070 Maintaining a drupal.org project with Git @endlink

Never renumber update functions.

Implementations of this hook should be placed in a mymodule.install file in
the same directory as mymodule.module. Drupal core's updates are implemented
using the system module as a name and stored in database/updates.inc.

Not all module functions are available from within a hook_update_N() function.
In order to call a function from your mymodule.module or an include file,
you need to explicitly load that file first.

During database updates the schema of any module could be out of date. For
this reason, caution is needed when using any API function within an update
function - particularly CRUD functions, functions that depend on the schema
(for example by using drupal_write_record()), and any functions that invoke
hooks. See @link update_api Update versions of API functions @endlink for
details.

The $sandbox parameter should be used when a multipass update is needed, in
circumstances where running the whole update at once could cause PHP to
timeout. Each pass is run in a way that avoids PHP timeouts, provided each
pass remains under the timeout limit. To signify that an update requires
at least one more pass, set $sandbox['#finished'] to a number less than 1
(you need to do this each pass). The value of $sandbox['#finished'] will be
unset between passes but all other data in $sandbox will be preserved. The
system will stop iterating this update when $sandbox['#finished'] is left
unset or set to a number higher than 1. It is recommended that
$sandbox['#finished'] is initially set to 0, and then updated each pass to a
number between 0 and 1 that represents the overall % completed for this
update, finishing with 1.

See the @link batch Batch operations topic @endlink for more information on
how to use the Batch API.

@param array $sandbox
  Stores information for multipass updates. See above for more information.

@throws DrupalUpdateException|PDOException
  In case of error, update hooks should throw an instance of DrupalUpdateException
  with a meaningful message for the user. If a database query fails for whatever
  reason, it will throw a PDOException.

@return string|null
  Optionally, update hooks may return a translated string that will be
  displayed to the user after the update has completed. If no message is
  returned, no message will be presented to the user.

@see batch
@see schemaapi
@see update_api
@see hook_update_last_removed()
@see update_get_update_list()
```

## Code

```php
function hook_update_N(&$sandbox) {
  // For non-multipass updates, the signature can simply be;
  // function hook_update_N() {

  // For most updates, the following is sufficient.
  db_add_field('mytable1', 'newcol', array('type' => 'int', 'not null' => TRUE, 'description' => 'My new integer column.'));

  // However, for more complex operations that may take a long time,
  // you may hook into Batch API as in the following example.

  // Update 3 users at a time to have an exclamation point after their names.
  // (They're really happy that we can do batch API in this hook!)
  if (!isset($sandbox['progress'])) {
    $sandbox['progress'] = 0;
    $sandbox['current_uid'] = 0;
    // We'll -1 to disregard the uid 0...
    $sandbox['max'] = db_query('SELECT COUNT(DISTINCT uid) FROM {users}')->fetchField() - 1;
  }

  $users = db_select('users', 'u')
    ->fields('u', array('uid', 'name'))
    ->condition('uid', $sandbox['current_uid'], '>')
    ->range(0, 3)
    ->orderBy('uid', 'ASC')
    ->execute();

  foreach ($users as $user) {
    $user->name .= '!';
    db_update('users')
      ->fields(array('name' => $user->name))
      ->condition('uid', $user->uid)
      ->execute();

    $sandbox['progress']++;
    $sandbox['current_uid'] = $user->uid;
  }

  $sandbox['#finished'] = empty($sandbox['max']) ? 1 : ($sandbox['progress'] / $sandbox['max']);

  // To display a message to the user when the update is completed, return it.
  // If you do not want to display a completion message, simply return nothing.
  return t('The update did what it was supposed to do.');

  // In case of an error, simply throw an exception with an error message.
  throw new DrupalUpdateException('Something went wrong; here is what you should do.');
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_update_N()".

_None found._

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
