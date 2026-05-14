# Tiny Notes App Example

This tiny example shows how AppForge artifacts might look.

## Concept

A simple notes app where users create, edit, and organize notes.

## Mode

Generic spec-first.

## Backend

Supabase, because notes need auth and simple CRUD.

## UX flow

- Launch.
- Login/signup.
- Notes list.
- Create note.
- Edit note.
- Delete note.

## Figma

Create screens for login, notes list, editor, empty state, and error state.

## Backend

Tables:

- `notes`
  - id
  - user_id
  - title
  - body
  - created_at
  - updated_at

## Native implementation

After design and API approval:

- SwiftUI notes list/editor.
- Compose notes list/editor.
