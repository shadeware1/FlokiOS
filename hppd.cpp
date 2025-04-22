#include <QApplication>
#include <QMainWindow>
#include <QPushButton>
#include <QMouseEvent>
#include <QLabel>
#include <QVBoxLayout>
#include <QDesktopWidget>
#include <QTimer>
#include <QWebEngineView>

class DraggableWindow : public QMainWindow {
    Q_OBJECT

public:
    DraggableWindow(const QString &title, const QString &url, QWidget *parent = nullptr) : QMainWindow(parent) {
        setWindowTitle(title);
        resize(400, 300);
        move(50, 40);

        QWidget *central = new QWidget(this);
        setCentralWidget(central);

        QVBoxLayout *layout = new QVBoxLayout(central);

        QLabel *label = new QLabel(title, this);
        layout->addWidget(label);

        QWebEngineView *web = new QWebEngineView(this);
        web->load(QUrl(url));
        layout->addWidget(web);

        QPushButton *btnClose = new QPushButton("Close", this);
        QPushButton *btnMin = new QPushButton("Minimize", this);
        QPushButton *btnMax = new QPushButton("Maximize", this);

        QHBoxLayout *btnLayout = new QHBoxLayout();
        btnLayout->addWidget(btnMin);
        btnLayout->addWidget(btnMax);
        btnLayout->addWidget(btnClose);
        layout->addLayout(btnLayout);

        connect(btnClose, &QPushButton::clicked, this, &QMainWindow::close);
        connect(btnMin, &QPushButton::clicked, this, &DraggableWindow::minimize);
        connect(btnMax, &QPushButton::clicked, this, &DraggableWindow::maximize);
    }

protected:
    void mousePressEvent(QMouseEvent *event) override {
        if (event->button() == Qt::LeftButton) {
            dragging = true;
            dragPos = event->globalPos() - frameGeometry().topLeft();
        }
    }

    void mouseMoveEvent(QMouseEvent *event) override {
        if (dragging) {
            move(event->globalPos() - dragPos);
        }
    }

    void mouseReleaseEvent(QMouseEvent *event) override {
        Q_UNUSED(event);
        dragging = false;
    }

private slots:
    void minimize() {
        resize(200, 50);
        move(10, QApplication::desktop()->screenGeometry().height() - 60);
    }

    void maximize() {
        if (isMaximized()) {
            resize(400, 300);
        } else {
            showMaximized();
        }
    }

private:
    bool dragging = false;
    QPoint dragPos;
};

int main(int argc, char *argv[]) {
    QApplication app(argc, argv);

    DraggableWindow *win = new DraggableWindow("My App", "https://example.com");
    win->show();

    return app.exec();
}

#include "main.moc"
