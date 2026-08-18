-- Add priority + due date to tasks
ALTER TABLE tasks ADD COLUMN priority TEXT DEFAULT 'medium';
ALTER TABLE tasks ADD COLUMN due_date TEXT;

CREATE INDEX idx_tasks_priority ON tasks (priority);
